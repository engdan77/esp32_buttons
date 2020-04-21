import sys

heart = """
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111110000000111111110000000111111111
1111111100000000011111100000000011111111
1111110000000000000110000000000000111111
1111100000111110000000000111110000011111
1111100000111110000000000111110000011111
1111000011111111100000111111111100001111
1111000011111111110000111111111100001111
1110000111111111111111111111111110000111
1110000111111111111111111111111110000111
1110000111111111111111111111111110000111
1110000111111111111111111111111110000111
1110000111111111111111111111111110000111
1111000011111111111111111111111100001111
1111100011111111111111111111111100011111
1111100011111111111111111111111100011111
1111100000111111111111111111110000011111
1111110000111111111111111111110000111111
1111111000011111111111111111100001111111
1111111100001111111111111111000011111111
1111111100000111111111111110000011111111
1111111111000001111111111000001111111111
1111111111000001111111111000001111111111
1111111111100000111111110000011111111111
1111111111111000001111100000111111111111
1111111111111000001111000001111111111111
1111111111111110000000000111111111111111
1111111111111110000000000111111111111111
1111111111111111100000011111111111111111
1111111111111111110000111111111111111111
1111111111111111110000111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
"""

audio = """
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111110111111111111111
1111111111111111111111100011111111111111
1111111111111111111011100000111111111111
1111111111111111110011110000001111111111
1111111111111111100011111000001111111111
1111111111111110000011111110000011111111
1111111111111110000011111111000011111111
1111111111111100000011111111100001111111
1111111111111000000011111111110001111111
1111111111110000000011110111110000111111
1111100000000000000011100011111000011111
1111100000000000000011100001111000011111
1111100000000000000011100001111100011111
1111100000000000000011100001111100011111
1111100000000000000011100001111100011111
1111100000000000000011100001111100011111
1111100000000000000011100001111100011111
1111100000000000000011100001111100011111
1111100000000000000011100001111000011111
1111100000000000000011100011111000011111
1111111111110000000011110111110000111111
1111111111111000000011111111110001111111
1111111111111100000011111111100001111111
1111111111111110000011111111000011111111
1111111111111110000011111110000011111111
1111111111111111100011110000001111111111
1111111111111111110011110000001111111111
1111111111111111111011100000111111111111
1111111111111111111111110011111111111111
1111111111111111111111110111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
"""

party = """
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111100111111111111111
1111111111111111111111100011111111111111
1111111111111111111111110001111111111111
1111111111111111101111111000111111111111
1111111111111111000111111000111111111111
1111111111111111100011111000111111001111
1111111111111111100011111000111110000111
1111111111111111100011110001110000000001
1111111111111111100011100001110000110011
1111111111111111000111000011100001111111
1111111111111111101110000111000011111111
1111111111110111111100000110000111111111
1111111111000001111100011000001111111111
1111111111000001111100111000011111111111
1111111111000000111111110000111111111111
1111111111000000011111100001110001111111
1111111111000000001111100011110000111111
1111111110000000000011111110000000001111
1111111110000000000011111110000110000111
1111111100000000000001111100001111000111
1111111100000000000000111110111111101111
1111111100000000000000011111111111111111
1111111000000000000000000111111111111111
1111111000000000000000000111111111111111
1111111000000000000000000011111111111111
1111110000000000000000000111111111111111
1111110000000000000000000111111111111111
1111100000000000000011111111111111111111
1111100000000000000111111111111111111111
1111100000000001111111111111111111111111
1111100000001111111111111111111111111111
1111100000111111111111111111111111111111
1111011111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
"""

poop = """
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111100011111111111111111111
1111111111111110000011111111111111111111
1111111111111110000011111111111111111111
1111111111111110000001111111111111111111
1111111111111100000000001111111111111111
1111111111111100000000000111111111111111
1111111111111000000000000000111111111111
1111111111111000000000000000111111111111
1111111111111000000000000000011111111111
1111111111000000000000000000111111111111
1111111111000000000000000000111111111111
1111111111000000000000000000001111111111
1111111111000110000000000111001111111111
1111111110011111100000011111110011111111
1111111110111111110000011111110011111111
1111111110111101110000111111110011111111
1111111000111000110000111000110001111111
1111111000111001110000111000110000111111
1111100000111111110000011111110000011111
1111100000011111100000011111110000011111
1111100000001111100000001111100000001111
1111100000000000000000000000000000001111
1111100000000000000000000000000000001111
1111100000000011111000111110000000001111
1111100000000011111111111110000000011111
1111100000000111111111111110000000011111
1111110000000001111111111000000000011111
1111111000000001111111111000000000011111
1111111000000000011111100000000001111111
1111111110000000000000000000000011111111
1111111111000000000000000000001111111111
1111111111111110000000000001111111111111
1111111111111111100000000111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
"""

smiley = """
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111100000011111111111111111
1111111111111110000000000111111111111111
1111111111100000000000000000011111111111
1111111111000000000000000000001111111111
1111111110000001111111111000000111111111
1111111100000111111111111110000011111111
1111111000001111111111111111000001111111
1111110000111111111111111111110000111111
1111100000111111111111111111110000011111
1111100001111111111111111111111000011111
1111100011111001111111111001111100011111
1111100011110000111111110000111100011111
1111000111110000011111100000111110001111
1111000111110000011111100000111110001111
1110000111110000111111110000111110000111
1110000111111111111111111111111110000111
1110000111111111111111111111111110000111
1110000111111111111111111111111110000111
1110000111111111111111111111111110000111
1110000111111111111111111111111110000111
1111000111110000000000000000111110001111
1111000111110000000000000000111110001111
1111100011111000000000000001111100011111
1111100011111000000000000001111100011111
1111100001111110000000000111111000011111
1111100000111111100000011111110000011111
1111110000111111111111111111110000111111
1111111000001111111111111111000001111111
1111111100000111111111111110000011111111
1111111110000001111111111000000111111111
1111111111000000000000000000001111111111
1111111111100000000000000000011111111111
1111111111111110000000000111111111111111
1111111111111111100000011111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
"""

tv = """
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111001111111111001111111111111
1111111111110001111111111000111111111111
1111111111110000111111110000111111111111
1111111111111000011111100001111111111111
1111111111111000001111000001111111111111
1111111111111110000000000111111111111111
1111111111111110000000000111111111111111
1111100000000000000000000000000000011111
1111000000000000000000000000000000001111
1110000000000000000000000000000000000111
1110000111111111111111111111000111000111
1110000111111111111111111111000111000111
1110000111111111111111111111000111000111
1110000111111111111111111111000000000111
1110000111111111111111111111000000000111
1110000111111111111111111111000111000111
1110000111111111111111111111000111000111
1110000111111111111111111111000111000111
1110000111111111111111111111000000000111
1110000111111111111111111111000000000111
1110000111111111111111111111000000000111
1110000111111111111111111111000000000111
1110000111111111111111111111000000000111
1110000111111111111111111111000000000111
1110000111111111111111111111000000000111
1110000111111111111111111111000000000111
1110000111111111111111111111000000000111
1110000000000000000000000000000000000111
1111100000000000000000000000000000011111
1111100000000000000000000000000000011111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
1111111111111111111111111111111111111111
"""

if sys.platform == "esp32":
    from mqtt_as_timeout import MQTTClient
    import machine
    import network
    from machine import unique_id
    from machine import Pin, I2C, PWM
    import esp32
    import utime as time
    import ssd1306

    # noinspection PyUnresolvedReferences
    from ubinascii import hexlify
    import uasyncio as asyncio
    from machine import Pin
    from ucollections import deque
else:
    import paho.mqtt.client as paho_client
    import asyncio
    import PySimpleGUI as sg
    from collections import deque
    import time
    import PySimpleGUI as sg
    from unittest.mock import Mock

    Pin = Mock()
    hexlify = Mock()
    unique_id = Mock()

import random

buttons_conf_other = {
    1: {
        "name": "1",
        "led_out": 16,
        "commands": {
            "TV 1<img>{}".format(tv): "/tv_command barn_tv",
            "TV 2<img>{}".format(tv): "/tv_command tv4",
            "TV 3<img>{}".format(tv): "/tv_command tv4",
            "Avbryt": "",
        },
        "enabled": True,
    },
    2: {
        "name": "2",
        "led_out": 16,
        "commands": {
            "Sound on<img>{}".format(audio): "/sound on",
            "Sound off<img>{}".format(audio): "/sound off",
            "Avbryt": "",
        },
        "enabled": True,
    },
    3: {"name": "3", "led_out": 17, "commands": {}, "enabled": True},
}

buttons_conf_esp32 = {
    26: {
        "name": "1",
        "led_out": 16,
        "commands": {"Barn TV<img>{}".format(tv): "/tv_command barn_tv", "TV4<img>{}".format(poop): "/tv_command tv4"},
        "enabled": True,
    },
    25: {"name": "2", "led_out": 19, "commands": {}, "enabled": False},
    33: {"name": "3", "led_out": 17, "commands": {}, "enabled": True},
    32: {"name": "4", "led_out": 5, "commands": {}, "enabled": True},
    35: {"name": "5-not-working", "led_out": 2, "commands": {}, "enabled": False},
    34: {"name": "6", "led_out": 18, "commands": {}, "enabled": True},
    39: {"name": "7", "led_out": 23, "commands": {}, "enabled": True},
}


def get_led_pin(conf, button_number=None):
    pins = []
    for k, v in conf.items():
        if 'led_out' in v and isinstance(v['led_out'], int):
            if button_number and v['name'] == str(button_number):
                return [v['led_out']]
            else:
                pins.append(v['led_out'])
    return pins


def chain(*p):
    for i in p:
        yield from i


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


class MyMQTT:
    def __init__(self, led_instance=None):
        self.mqtt_config = {
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
            "default_topic": "/esp32_buttons",
        }
        self.led = led_instance
        self.loop = asyncio.get_event_loop()
        print("start mqtt client")
        if sys.platform == "esp32":
            MQTTClient.DEBUG = True  # Optional
            self.mqtt_client = MQTTClient(self.mqtt_config)
        else:
            self.mqtt_client = paho_client.Client()
            self.mqtt_client.username_pw_set(
                self.mqtt_config["user"], self.mqtt_config["password"]
            )
            self.loop.create_task(self.connect())

    async def connect(self):
        if sys.platform == "esp32":
            if self.led:
                self.loop.create_task(
                    self.led.start_pulse([self.led.red, self.led.green])
                )
            try:
                await self.mqtt_client.connect()
            except OSError as e:
                print("failed connecting to mqtt: {}".format(e))
                await self.led.state(True, self.led.red, 2)
            else:
                print("connected successfully")
                await self.mqtt_client.publish(
                    self.mqtt_config["default_topic"],
                    "connected",
                    retain=False,
                    qos=1,
                    timeout=None,
                )
                print("MQTT ok")
                await self.led.state(True, self.led.green, 2)
        else:
            self.mqtt_client.connect(self.mqtt_config["server"])

    def disconnect(self):
        self.mqtt_client.disconnect()

    def publish(self, message, topic=None):
        self.mqtt_client.publish(
            topic if topic else self.mqtt_config["default_topic"], message
        )


class Buttons:
    def __init__(self, button_config, max_queue=10):
        self.config = button_config
        self.q = deque((), 10)
        self.enabled = True
        _loop = asyncio.get_event_loop()
        _loop.create_task(self.loop_process())

    async def loop_process(self, sleep_time=0.01, debounce_times=15):
        if sys.platform == "esp32":
            while self.enabled:
                for k, v in self.config.items():
                    p = Pin(k, Pin.IN)
                    if p.value():
                        # debounce
                        active = 0
                        for _ in range(debounce_times):
                            if p.value():
                                active += 1
                            await asyncio.sleep(sleep_time)
                        if active == debounce_times:
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
        self.x_text = 0
        self.y_text = 0
        self.x_image = 10
        self.y_image = 10

        if self.p == "esp32":
            i2c = I2C(-1, scl=Pin(self.scl_pin), sda=Pin(self.sda_pin))
            self.oled = ssd1306.SSD1306_I2C(self.width, self.height, i2c)
        self.clear()
        _loop = asyncio.get_event_loop()
        _loop.create_task(self.loop_process())

    def print(self, text):
        self.q.append(text)
        # print('adding text "{}" -> {}'.format(text, self.q))

    def clear(self):
        if self.p == "esp32":
            self.oled.fill(0)
            self.oled.show()
        else:
            self.print("")

    def turn_off(self):
        self.oled.poweroff()

    async def loop_process(self, sleep_time=0.1):
        print("starting screen loop")
        # this will be replaced by true hw
        while self.enabled:
            if self.q:
                if self.p == "esp32":
                    # print("found new message in queue")
                    self._print_oled()
                else:
                    self._print_mock()
            await asyncio.sleep(sleep_time)

    def _print_mock(self):
        self.text[0] = self.q.popleft()

    def _print_oled(self):
        text = self.q.popleft()
        # print("printing {} to oled".format(text))

        both = text.split("<img>")
        img = None
        if len(both) == 2:
            text, img = both
        else:
            (text,) = both

        self.oled.fill(0)
        self.oled.text(text, self.x_text, self.y_text)

        if img:
            self._display_image(img)

        self.oled.show()

    def _display_image(self, img, x_offset=0, y_offset=10):
        for y, row in enumerate(img.strip().split('\n')):
            for x, c in enumerate(row):
                self.oled.pixel(x_offset + x + self.x_image, y_offset + y + self.y_image, (1, 0)[int(c)])
        self.oled.show()

    def stop(self):
        self.enabled = False


def turn_on(pin):
    Pin(pin, Pin.OUT).value(True)


def turn_off(pin):
    Pin(pin, Pin.OUT).value(False)


class Led:
    def __init__(self, button_pins=[], pin_red=13, pin_green=12, pin_blue=14, frequency=64, interval=0.05):
        self.red = pin_red
        self.green = pin_green
        self.blue = pin_blue
        self.pulse_on = False
        self.frequency = frequency
        self.button_pins = button_pins
        self.led_timers = {}
        self.enabled = True
        self.turn_all_off(force=True)
        asyncio.get_event_loop().create_task(self.timer_loop(interval))

    async def start_pulse(self, colors, speed=2):
        self.pulse_on = True
        colors = [colors] if isinstance(colors, int) else colors
        self.turn_all_off()
        leds = []
        for p in colors:
            leds.append(PWM(Pin(p), self.frequency))
        while self.pulse_on:
            for duty_cycle in chain(range(0, 128, speed), range(128, 0, -speed)):
                for led in leds:
                    led.duty(duty_cycle)
                await asyncio.sleep(0.010)

    def stop_pulse(self):
        self.pulse_on = False
        self.turn_all_off()

    async def state(self, on_state, pins, for_time=None):
        pins = [pins] if isinstance(pins, int) else pins
        self.turn_all_off()
        if not on_state:
            for p in pins:
                self.remove_timer(p)
                turn_off(p)
        else:
            for p in pins:
                turn_on(p)
                if for_time:
                    self.add_timer(p, for_time)

    def add_timer(self, pin, for_time):
        if for_time >= self.led_timers.get(pin, 0):
            self.led_timers[pin] = for_time

    def remove_timer(self, pin):
        try:
            self.led_timers.pop(pin)
        except KeyError:
            pass

    async def timer_loop(self, interval=0.5):
        while self.enabled:
            for p, t in self.led_timers.items():
                if float(t) <= float(0):
                    turn_off(p)
                    self.led_timers.pop(p)
                    continue
                self.led_timers[p] = float(self.led_timers[p]) - float(interval)
            await asyncio.sleep(interval)

    def stop(self):
        self.turn_all_off(force=True)
        self.enabled = False

    def turn_all_off(self, force=True):
        for p in self.led_timers.keys():
            turn_off(p)
        if force:
            for p in (self.red, self.green, self.blue) + tuple(self.button_pins):
                turn_off(p)


class Controller:
    def __init__(
            self,
            button_instance: Buttons,
            screen_instance: Screen,
            led_instance: Led = None,
            mqtt_instance: MyMQTT = None,
            inactivity_timeout = 20
    ):
        self.b = button_instance
        self.s = screen_instance
        self.l = led_instance
        self.m = mqtt_instance
        self.enabled = True
        self.option_timout = 5
        self.option_timers = {}
        self.current_button = 0
        self.current_option = -1
        self.last_button_pressed = None
        self.inactivity_timeout = self.current_inactivity_countdown = inactivity_timeout
        asyncio.get_event_loop().create_task(self.loop_process())
        if sys.platform == 'esp32':
            asyncio.get_event_loop().create_task(self.inactivity_timeout_loop())

    async def inactivity_timeout_loop(self):
        while self.enabled and self.current_inactivity_countdown >= 0:
            self.current_inactivity_countdown -= 1
            await asyncio.sleep(1)
        self.s.turn_off()
        self.m.disconnect()
        self.l.stop()
        wakeup_pins = self.b.config.keys()
        esp32_deep_sleep(wakeup_pins)

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
        if sys.platform == 'esp32':
            self.current_inactivity_countdown = self.inactivity_timeout
            if self.last_button_pressed is None or self.last_button_pressed == button_key:
                all_button_leds = get_led_pin(self.b.config)
                await self.l.state(False, all_button_leds)
                self.last_button_pressed = button_key
            p = get_led_pin(self.b.config, button_key)
            _loop = asyncio.get_event_loop()
            _loop.create_task(self.l.state(True, p, 5))
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
        # self.s.print("{} [{}]".format(next_option, self.option_timout))

        # remember which button was pressed
        self.current_button = button_key

        _loop = asyncio.get_event_loop()
        _loop.create_task(self.start_timer(next_option))

    async def start_timer(self, option_text):
        self.option_timers = {}
        ref = random.randint(1, 1000000)
        self.option_timers[ref] = self.option_timout
        timer_left = self.option_timers[ref]
        while ref in self.option_timers and timer_left >= 1:
            timer_left -= 1
            if "<img>" in option_text:
                self.s.print(
                    option_text.replace("<img>", " [{}] <img>".format(timer_left + 1))
                )
            else:
                self.s.print("{} [{}]".format(option_text, timer_left + 1))
            await asyncio.sleep(1)
            # print("count down current option timers {}".format(self.option_timers))
        if ref in self.option_timers:
            # this means no other key been pressed and timed out
            print(
                "trigger button {} option {}".format(
                    self.current_button, self.current_option
                )
            )
            if self.m:
                msg = "{},{}".format(self.current_button, self.current_option)
                print('mqtt publish {}'.format(msg))
                self.m.publish(msg)

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
    loop = asyncio.get_event_loop()
    buttons = Buttons(buttons_conf_esp32)
    led_pins = get_led_pin(buttons_conf_esp32)
    led = Led(led_pins)
    mqtt = MyMQTT(led)
    loop.create_task(mqtt.connect())

    screen = Screen()
    screen.print('Daniels knappar')
    Controller(buttons, screen, led, mqtt)

    buttons_pressed = buttons.get_pressed()
    print(buttons_pressed)

    # await asyncio.sleep(60)
    # screen.print("ZZzzz")
    # await asyncio.sleep(3)
    # screen.turn_off()
    # mqtt.disconnect()
    # led.stop()
    # await asyncio.sleep(1)
    # machine.reset()


def init_other():
    text_ref = [""]
    led = Led()
    buttons = Buttons(buttons_conf_other)
    screen = Screen(text_ref)
    mqtt = MyMQTT()
    Controller(buttons, screen, led, mqtt)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(other_loop(buttons, text_ref, mqtt))


def draw_image(image_data, graph_instance, size=1):
    pixel_rows = reversed(image_data.strip().split("\n"))
    row_idx, col_idx = (0, 0)
    for row in pixel_rows:
        row_idx += size
        col_idx = 0
        for col in row:
            col_idx += size
            if col == "0":
                graph_instance.DrawPoint((col_idx, row_idx), size, color="green")


async def other_loop(b, _text, mqtt):
    layout = [
        [sg.Text("Press 1 or 2")],
        [sg.Text("", size=(18, 1), key="text")],
        [
            sg.Graph(
                canvas_size=(40, 40),
                graph_bottom_left=(0, 0),
                graph_top_right=(40, 40),
                background_color="white",
                key="graph",
            )
        ],
        [sg.Button("OK", key="OK")],
    ]

    window = sg.Window(
        "Keyboard Test", layout, return_keyboard_events=True, use_default_focus=False
    )
    while True:
        event, values = window.read(timeout=100)
        await asyncio.sleep(0)

        both = _text[0].split("<img>")
        img = None
        if len(both) == 2:
            text, img = both
        else:
            (text,) = both

        window["text"].update(value=text)
        window["graph"].Erase()
        if img:
            draw_image(img, window["graph"])

        if event in ("OK", None):
            print(event, "exiting")
            break
        if event is not None:
            if event in ("1", "2"):
                print("add {} to queue".format(event))
                b.mock_press(event)
    window.close()
    mqtt.disconnect()


if __name__ == "__main__":
    if sys.platform == "esp32":
        init_esp32()
    else:
        init_other()
