import machine
from machine import Pin, I2C
import esp32
import utime
from umqtt.robust import MQTTClient
import network
import ssd1306


def mqtt_send(topic, msg, server, client_id, user, password):
    client = MQTTClient(client_id, server, user=user, password=password)
    client.connect()
    client.publish(topic, msg)
    client.disconnect()


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


def main():
    wakeup_pin = 26
    boot_value = machine.Pin(wakeup_pin, machine.Pin.IN).value()
    print(boot_value)

    # with open('pin.log', 'w') as f:
    #     f.write('{},'.format(boot_value))

    blink(1, 2, 2)
    light_on(boot_value)
    display_text("button pressed " + str(boot_value))

    utime.sleep(3)

    wifi_ssid, password = ("***REMOVED***", "***REMOVED***")
    wifi_connect(wifi_ssid, password)
    utime.sleep(2)

    mqtt_send(
        "/esp32/pin",
        str(boot_value),
        "10.1.1.5",
        "esp32",
        user="homeassistant",
        password="***REMOVED***",
    )
    utime.sleep(2)

    boot_pin = machine.Pin(wakeup_pin, machine.Pin.IN)
    esp32.wake_on_ext0(pin=boot_pin, level=esp32.WAKEUP_ANY_HIGH)
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


if __name__ == "__main__":
    # pass
    main()
