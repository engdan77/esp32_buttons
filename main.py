from mqtt_as_timeout import MQTTClient
import machine
from machine import Pin, I2C
import esp32
import utime
import network
import ssd1306
from ubinascii import hexlify
from machine import unique_id
import uasyncio as asyncio


# led in 26, 25, 33, 32, 35, 34, 39
# led out 12, 14, 27
# led out - 23, 19, 18, 5, 17, 16, 4


buttons = {
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
    client_instance.publish("/esp32/button", "connected", retain=False, qos=1, timeout=None)


def blink(times=5, pin=2, time_between=0.3):
    led = machine.Pin(pin, machine.Pin.OUT)
    for _ in range(times):
        led.value(not led.value())
        utime.sleep(time_between)


def light_on(on=True, period=None, pin=2):
    pin = [pin] if type(pin) is int else pin
    for p in pin:
        machine.Pin(p, machine.Pin.OUT).value(bool(on))
    if period:
        utime.sleep(period)
        for p in pin:
            machine.Pin(p, machine.Pin.OUT).value(False)


def restart_wifi(sta_if):
    sta_if.disconnect()
    sta_if.active(False)
    utime.sleep(1)
    sta_if.active(True)
    utime.sleep(1)
    sta_if.connect("***REMOVED***", "***REMOVED***")


def wifi_connect(ssid, password, pin_working=12, pin_connected=14):
    sta_if = network.WLAN(network.STA_IF)
    if sta_if.isconnected():
        print("Already connected")
        return
    sta_if.active(True)
    sta_if.connect(ssid, password)

    repeats = 0
    while not sta_if.isconnected():
        repeats += 1
        utime.sleep(0.3)
        light_on(True, 0.2, pin_working)
        if repeats >= 8:
            repeats = 0
            restart_wifi(sta_if)
    light_on(True, None, pin_connected)


def get_buttons_pressed(button_config):
    buttons_pressed = []
    for k, v in button_config.items():
        if Pin(p, Pin.IN).value():
            buttons_pressed.append(v.get('name', ''))
    return buttons_pressed


def get_wakeup_pins(pin_list):
    return [Pin(p, Pin.IN) for p in pin_list]


async def start_main(mqtt_client):
    button_pins = list(buttons.keys())
    buttons_pressed = get_buttons_pressed(button_pins)
    t = ",".join(buttons_pressed)
    print('buttons pressed: {}'.format(t))

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
    wakeup_pins = get_wakeup_pins(button_pins)
    clear_screen()
    esp32.wake_on_ext1(wakeup_pins, esp32.WAKEUP_ANY_HIGH)
    machine.deepsleep()


def display_text(input_text, scl_pin=22, sda_pin=21):
    # ESP32 Pin assignment
    i2c = I2C(-1, scl=Pin(scl_pin), sda=Pin(sda_pin))
    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    oled.fill(0)
    oled.text(input_text, 0, 0)
    oled.show()


def clear_screen(scl_pin=22, sda_pin=21):
    i2c = I2C(-1, scl=Pin(scl_pin), sda=Pin(sda_pin))
    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    oled.fill(0)


def start():
    config = {
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
    mqtt_client = MQTTClient(config)
    print("About to run.")
    try:
        loop.run_until_complete(start_main(mqtt_client=mqtt_client))
    finally:
        mqtt_client.close()


if __name__ == "__main__":
    start()
    # pass

