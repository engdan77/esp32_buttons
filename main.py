import machine
import esp32
import utime
from umqtt.robust import MQTTClient
import network


def mqtt_send(topic,
              msg,
              server,
              client_id,
              user,
              password):
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
    sta_if.connect('***REMOVED***', '***REMOVED***')

def wifi_connect():
    sta_if = network.WLAN(network.STA_IF)
    if sta_if.isconnected():
        print("Already connected")
        return
    sta_if.active(True)
    sta_if.connect('***REMOVED***', '***REMOVED***')

    repeats = 0
    while not sta_if.isconnected():
        repeats += 1
        utime.sleep(0.3)
        light_on(True, 0.2, 27)
        if repeats >= 8:
            repeats = 0
            restart_wifi(sta_if)
    light_on(True, None, 32)


def main():
    boot_value = machine.Pin(36, machine.Pin.IN).value()

    # with open('pin.log', 'w') as f:
    #     f.write('{},'.format(boot_value))

    blink(1, 2, 0.1)

    light_on(boot_value)

    utime.sleep(3)

    wifi_connect()
    utime.sleep(2)
    light_on(True, 2, [27, 32])

    mqtt_send('/esp32/pin', str(boot_value), '10.1.1.1', 'esp32', user='homeassistant', password='***REMOVED***')

    utime.sleep(2)

    boot_pin = machine.Pin(36, machine.Pin.IN)
    esp32.wake_on_ext0(pin=boot_pin, level=esp32.WAKEUP_ANY_HIGH)
    machine.deepsleep()


if __name__ == '__main__':
    # pass
    main()
