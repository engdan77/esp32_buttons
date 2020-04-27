from images import audio, poop, tv

buttons_conf_other = {
    1: {
        "name": "1",
        "led_out": 16,
        "commands": {
            "TV 1<img>{}".format(tv): "barn_tv",
            "TV 2<img>{}".format(tv): "tv2",
            "TV 3<img>{}".format(tv): "func:start_web_repl",
            "Avbryt": "",
        },
        "enabled": True,
    },
    2: {
        "name": "2",
        "led_out": 16,
        "commands": {
            "Sound on<img>{}".format(audio): "sound_on",
            "Sound off<img>{}".format(audio): "sound_off",
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
        "commands": {"Barn TV<img>{}".format(tv): "barn_tv", "TV4<img>{}".format(poop): "tv4"},
        "enabled": True,
    },
    25: {"name": "2", "led_out": 19, "commands": {}, "enabled": False},
    33: {"name": "3", "led_out": 17, "commands": {"Knapp 3": "button3"}, "enabled": True},
    32: {"name": "4", "led_out": 5, "commands": {"Knapp 4": "button4_led_always_on"}, "enabled": True},
    35: {"name": "5-not-working", "led_out": 2, "commands": {}, "enabled": False},
    34: {"name": "6", "led_out": 18, "commands": {"Knapp 6": "button6"}, "enabled": True},
    39: {"name": "7", "led_out": 23, "commands": {"Knapp 7": "func:start_web_repl"}, "enabled": True},
}


mqtt_user = 'homeassistant'
mqtt_pass = '***REMOVED***'
ssid = '***REMOVED***'
wifi_pw = '***REMOVED***'
client_id = 'my_buttons'