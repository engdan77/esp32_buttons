import sys

if sys.platform == "esp32":
    import PySimpleGUI as sg
    from mqtt_as_timeout import MQTTClient
    import machine
    from machine import unique_id
    from machine import Pin, I2C
    import esp32
    import utime as time
    import ssd1306
    from ubinascii import hexlify
    import uasyncio as asyncio
else:
    import asyncio
    from collections import deque
    import time
    import PySimpleGUI as sg

try:
    import Pin
except ModuleNotFoundError:
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


def wifi_coro(connected_bool):
    print("wifi connected {}".format(connected_bool))


def connect_coro(client_instance):
    print("connected to broker")
    client_instance.publish(
        "/esp32/button", "connected", retain=False, qos=1, timeout=None
    )


class Buttons:
    def __init__(self, button_config, max_queue=10):
        self.config = button_config
        self.q = deque(maxlen=max_queue)
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
        self.q = deque(maxlen=max_queue)
        self.scl_pin = scl_pin
        self.sda_pin = sda_pin
        self.width = width
        self.height = height
        self.enabled = True
        self.text = text
        _loop = asyncio.get_event_loop()
        _loop.create_task(self.loop_process())

    def print(self, text):
        self.q.append(text)
        print('adding text "{}" -> {}'.format(text, self.q))

    def clear(self):
        self.print("")

    async def loop_process(self, sleep_time=0.1):
        print("starting screen loop")
        # this will be replaced by true hw
        while self.enabled:
            if self.q:
                if sys.version == "esp32":
                    self._print_oled()
                else:
                    self._print_mock()
            await asyncio.sleep(sleep_time)

    def _print_mock(self):
        self.text[0] = self.q.popleft()

    def _print_oled(self):
        text = self.q.popleft()
        i2c = I2C(-1, scl=Pin(self.scl_pin), sda=Pin(self.sda_pin))
        oled_width = self.width
        oled_height = self.height
        oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
        oled.fill(0)
        oled.text(text, 0, 0)
        oled.show()

    def stop(self):
        self.enabled = False


class Led:
    def __init__(self, pin_red=12, pin_green=13, pin_blue=14):
        self.r = pin_red
        self.g = pin_green
        self.b = pin_blue

    def color(self, color, state):
        pass


class Controller:
    def __init__(self, button_instance: Buttons, screen_instance: Screen, led_instance):
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
        print("print and wait")
        options = self.b.config.get(button_key, None)
        if not options:
            return
        if not self.current_button == button_key or self.current_option + 1 >= len(
            options["commands"]
        ):
            # if you switch button with new options
            self.current_option = -1

        # switch to next option
        self.current_option += 1
        self.s.print(list(options["commands"].keys())[self.current_option])

        # remember which button was pressed
        self.current_button = button_key

        _loop = asyncio.get_event_loop()
        _loop.create_task(self.start_timer())

    async def start_timer(self):
        self.option_timers = {}
        ref = time.time()
        self.option_timers[ref] = self.option_timout
        while ref in self.option_timers and self.option_timers[ref] >= 1:
            self.option_timers[ref] -= 1
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
            self.b.q.clear()
            self.s.clear()
            self.option_timers.pop(ref)
        else:
            print("key pressed and this coroutine aborted")

    def stop(self):
        self.enabled = False


async def mqtt_connect():
    try:
        await mqtt_client.connect()
    except OSError as e:
        print("failed connecting to mqtt: {}".format(e))
        display_text("mqtt error")
    else:
        for b in buttons_pressed:
            mqtt_client.publish("/esp32/button", b, retain=False, qos=1, timeout=None)


def get_buttons_pressed(button_config):
    buttons_pressed = []
    for k, v in button_config.items():
        if Pin(p, Pin.IN).value():
            buttons_pressed.append(v.get("name", ""))
    return buttons_pressed


def get_wakeup_pins(pin_list):
    return [Pin(p, Pin.IN) for p in pin_list]


def esp32_deep_sleep(button_pins):
    wakeup_pins = get_wakeup_pins(button_pins)
    esp32.wake_on_ext1(wakeup_pins, esp32.WAKEUP_ANY_HIGH)
    machine.deepsleep()


def init_esp32():
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
        "will": ("result", "Goodbye cruel world!", False, 0),
        "subs_cb": lambda *_: None,
        "wifi_coro": wifi_coro,
        "connect_coro": connect_coro,
        "ssid": "***REMOVED***",
        "wifi_pw": "***REMOVED***",
    }
    loop = asyncio.get_event_loop()
    print("Setting up client.")
    MQTTClient.DEBUG = True  # Optional
    mqtt_client = MQTTClient(mqtt_config)
    print("About to run.")
    try:
        loop.run_until_complete(start_esp32_loop(mqtt_client=mqtt_client))
    finally:
        mqtt_client.close()


async def start_esp32_loop(mqtt_client):
    button_pins = list(buttons.keys())
    buttons_pressed = get_buttons_pressed(button_pins)
    t = ",".join(buttons_pressed)
    print("buttons pressed: {}".format(t))

    blink(1, 2, 2)
    display_text(str(t))
    utime.sleep(3)

    try:
        await mqtt_client.connect()
    except OSError as e:
        print("failed connecting to mqtt: {}".format(e))
        display_text("mqtt error")
    else:
        for b in buttons_pressed:
            mqtt_client.publish("/esp32/button", b, retain=False, qos=1, timeout=None)

    utime.sleep(2)
    print("going deep sleep")
    print(button_pins)
    blink(5, 2, 0.5)


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
                print(f"add {event} to queue")
                b.mock_press(event)
    window.close()


if __name__ == "__main__":
    if sys.platform == "esp32":
        init_esp32()
    else:
        init_other()
