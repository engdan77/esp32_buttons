import sys

if sys.platform == "esp32":
    from mqtt_as_timeout import MQTTClient
    import machine
    import network
    from machine import unique_id
    from machine import Pin, I2C
    import esp32
    import utime as time
    import ssd1306

    # noinspection PyUnresolvedReferences
    from ubinascii import hexlify
    import uasyncio as asyncio
    from machine import Pin
    from ucollections import deque
else:
    import asyncio
    import PySimpleGUI as sg
    from collections import deque
    import time
    import PySimpleGUI as sg
    from unittest.mock import Mock

    Pin = Mock()
    hexlify = Mock()
    unique_id = Mock()

buttons_conf_other = {
    1: {
        "name": "1",
        "led_out": 16,
        "commands": {
            "TV 1": "/tv_command barn_tv",
            "TV2": "/tv_command tv4",
            "TV3": "/tv_command tv4",
            "Avbryt": "",
        },
        "enabled": True,
    },
    2: {
        "name": "2",
        "led_out": 16,
        "commands": {"Sound on": "/sound on", "Sound off": "/sound off"},
        "enabled": True,
    },
    3: {"name": "3", "led_out": 17, "commands": {}, "enabled": True},
}

buttons_conf_esp32 = {
    26: {
        "name": "1",
        "led_out": 16,
        "commands": {"Barn TV": "/tv_command barn_tv", "TV4": "/tv_command tv4"},
        "enabled": True,
    },
    25: {"name": "2", "led_out": 19, "commands": {}, "enabled": False},
    33: {"name": "3", "led_out": 17, "commands": {}, "enabled": True},
    32: {"name": "4", "led_out": 5, "commands": {}, "enabled": True},
    35: {"name": "5-not-working", "led_out": 2, "commands": {}, "enabled": False},
    34: {"name": "6", "led_out": 18, "commands": {}, "enabled": True},
    39: {"name": "7", "led_out": 23, "commands": {}, "enabled": True},
}


def empty_queue(queue):
    while True:
        try:
            queue.popleft()
        except IndexError:
            break


async def wifi_coro(connected_bool):
    print("wifi connected {}".format(connected_bool))


async def connect_coro(client_instance):
    print("connected to broker")
    client_instance.publish(
        "/esp32/button", "established", retain=False, qos=1, timeout=None
    )


class Buttons:
    def __init__(self, button_config, max_queue=10):
        self.config = button_config
        self.q = deque((), 10)
        self.enabled = True
        _loop = asyncio.get_event_loop()
        _loop.create_task(self.loop_process())

    async def loop_process(self, sleep_time=0.1):
        if sys.platform == "esp32":
            while self.enabled:
                for k, v in self.config.items():
                    if Pin(k, Pin.IN).value():
                        self.q.append(v.get("name", ""))
                await asyncio.sleep(sleep_time)

    def get_pressed(self):
        return self.q.popleft() if self.q else None

    def mock_press(self, key):
        # this is for external services to mimic button pressed
        self.q.append(key)
        print("button queue {} -> {}".format(key, self.q))

    def stop(self):
        self.enabled = False


class Screen:
    def __init__(
        self, text=[""], scl_pin=22, sda_pin=21, width=128, height=64, max_queue=10
    ):
        self.q = deque((), 10)
        self.scl_pin = scl_pin
        self.sda_pin = sda_pin
        self.width = width
        self.height = height
        self.enabled = True
        self.text = text
        self.p = sys.platform
        if self.p == "esp32":
            i2c = I2C(-1, scl=Pin(self.scl_pin), sda=Pin(self.sda_pin))
            self.oled = ssd1306.SSD1306_I2C(self.width, self.height, i2c)
        self.clear()
        _loop = asyncio.get_event_loop()
        _loop.create_task(self.loop_process())

    def print(self, text):
        self.q.append(text)
        print('adding text "{}" -> {}'.format(text, self.q))

    def clear(self):
        if self.p == "esp32":
            self.oled.fill(0)
            self.oled.show()
        else:
            self.print("")

    async def loop_process(self, sleep_time=0.1):
        print("starting screen loop")
        # this will be replaced by true hw
        while self.enabled:
            if self.q:
                if self.p == "esp32":
                    print("found new message in queue")
                    self._print_oled()
                else:
                    self._print_mock()
            await asyncio.sleep(sleep_time)

    def _print_mock(self):
        self.text[0] = self.q.popleft()

    def _print_oled(self):
        text = self.q.popleft()
        print("printing {} to oled".format(text))
        self.oled.fill(0)
        self.oled.text(text, 0, 0)
        self.oled.show()

    def stop(self):
        self.enabled = False


def turn_on(pin):
    Pin(pin, Pin.OUT).value(True)


class Led:
    def __init__(self, pin_red=12, pin_green=13, pin_blue=14):
        self.red = pin_red
        self.green = pin_green
        self.blue = pin_blue

    def state(self, on_state, colors, for_time=None):
        colors = [colors] if isinstance(colors, int) else colors
        self.turn_all_off()
        if not on_state:
            return
        else:
            for p in colors:
                turn_on(p)
            if for_time:
                time.sleep(for_time)
                self.turn_all_off()

    def turn_all_off(self):
        for p in (self.red, self.green, self.blue):
            Pin(p, Pin.OUT).value(False)


class Controller:
    def __init__(
        self,
        button_instance: Buttons,
        screen_instance: Screen,
        led_instance: Led = None,
    ):
        self.b = button_instance
        self.s = screen_instance
        self.l = led_instance
        self.enabled = True
        self.option_timout = 5
        self.option_timers = {}
        self.current_button = 0
        self.current_option = -1
        _loop = asyncio.get_event_loop()
        _loop.create_task(self.loop_process())

    async def loop_process(self, sleep_time=0.1):
        while self.enabled:
            button_pressed = self.b.get_pressed()
            if button_pressed:
                b = int(button_pressed)
                await self.print_and_wait(b)
            await asyncio.sleep(sleep_time)

    async def print_and_wait(self, button_key):
        print(
            "button {} ({}) pressed - print and wait".format(
                button_key, type(button_key)
            )
        )
        print("config")
        print(self.b.config)
        try:
            options = next(
                iter(
                    [
                        v
                        for k, v in self.b.config.items()
                        if str(v["name"]) == str(button_key)
                    ]
                )
            )
        except StopIteration:
            options = None
        if not options:
            print("button not found in config")
            return
        if not self.current_button == button_key or self.current_option + 1 >= len(
            options["commands"]
        ):
            # if you switch button with new options
            self.current_option = -1

        # switch to next option
        self.current_option += 1
        next_option = list(options["commands"].keys())[self.current_option]
        self.s.print("{} [{}]".format(next_option, self.option_timout))

        # remember which button was pressed
        self.current_button = button_key

        _loop = asyncio.get_event_loop()
        _loop.create_task(self.start_timer(next_option))

    async def start_timer(self, option_text):
        self.option_timers = {}
        ref = time.time()
        self.option_timers[ref] = self.option_timout
        timer_left = self.option_timers[ref]
        while ref in self.option_timers and timer_left >= 1:
            timer_left -= 1
            self.s.print("{} [{}]".format(option_text, timer_left + 1))
            await asyncio.sleep(1)
        if ref in self.option_timers:
            # this means no other key been pressed and timed out
            print(
                "trigger button {} option {}".format(
                    self.current_button, self.current_option
                )
            )
            self.current_option = 0
            self.current_button = 0
            empty_queue(self.b.q)
            self.s.clear()
            self.option_timers.pop(ref)
        else:
            print("key pressed and this coroutine aborted")

    def stop(self):
        self.enabled = False


def get_buttons_pressed(button_config):
    buttons_pressed = []
    for k, v in button_config.items():
        if Pin(k, Pin.IN).value():
            buttons_pressed.append(v.get("name", ""))
    return buttons_pressed


def get_wakeup_pins(pin_list):
    return [Pin(p, Pin.IN) for p in pin_list]


def esp32_deep_sleep(button_pins):
    wakeup_pins = get_wakeup_pins(button_pins)
    esp32.wake_on_ext1(wakeup_pins, esp32.WAKEUP_ANY_HIGH)
    machine.deepsleep()


def init_esp32():
    loop = asyncio.get_event_loop()
    loop.create_task(start_esp32_loop())
    loop.run_forever()


async def start_esp32_loop():
    print("start esp32 loop")
    buttons = Buttons(buttons_conf_esp32)
    screen = Screen()
    Controller(buttons, screen)

    mqtt_config = {
        "client_id": hexlify(unique_id()),
        "server": "10.1.1.5",
        "port": 0,
        "user": "homeassistant",
        "password": "***REMOVED***",
        "keepalive": 60,
        "ping_interval": 0,
        "ssl": False,
        "ssl_params": {},
        "response_time": 10,
        "clean_init": True,
        "clean": True,
        "max_repubs": 4,
        "will": None,
        "subs_cb": lambda *_: None,
        "wifi_coro": wifi_coro,
        "connect_coro": connect_coro,
        "ssid": "***REMOVED***",
        "wifi_pw": "***REMOVED***",
    }
    print("start mqtt client")
    MQTTClient.DEBUG = True  # Optional
    mqtt_client = MQTTClient(mqtt_config)

    # buttons_pressed = get_buttons_pressed(buttons_conf_esp32)
    buttons_pressed = buttons.get_pressed()
    print(buttons_pressed)

    screen.print("Connect MQTT")

    try:
        await mqtt_client.connect()
    except OSError as e:
        m = "failed connecting to mqtt: {}".format(e)
        screen.print("MQTT fail")
    else:
        print("connected successfully")
        await mqtt_client.publish(
            "/esp32/button", "connected", retain=False, qos=1, timeout=None
        )
        screen.print("MQTT ok")

    await asyncio.sleep(60)
    screen.print("ZZzzz")
    await asyncio.sleep(3)
    screen.clear()
    machine.reset()


def init_other():
    text_ref = [""]
    led = Led()
    buttons = Buttons(buttons_conf_other)
    screen = Screen(text_ref)
    Controller(buttons, screen, led)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(other_loop(buttons, text_ref))


async def other_loop(b, _text):
    layout = [
        [sg.Text("Press 1 or 2")],
        [sg.Text("", size=(18, 1), key="text")],
        [sg.Button("OK", key="OK")],
    ]

    window = sg.Window(
        "Keyboard Test", layout, return_keyboard_events=True, use_default_focus=False
    )
    while True:
        event, values = window.read(timeout=100)
        await asyncio.sleep(0)

        window["text"].update(value=_text[0])

        if event in ("OK", None):
            print(event, "exiting")
            break
        if event is not None:
            if event in ("1", "2"):
                print("add {} to queue".format(event))
                b.mock_press(event)
    window.close()


if __name__ == "__main__":
    if sys.platform == "esp32":
        init_esp32()
    else:
        init_other()
