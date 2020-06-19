import sys

if sys.platform == "esp32":
    from ucollections import OrderedDict
else:
    from collections import OrderedDict

buttons_conf_other = {
    1: {
        "name": "1",
        "led_out": 16,
        "commands": {
            "TV 1<img>tv": "barn_tv",
            "TV 2<img>tv": "tv2",
            "TV 3<img>poop": "func:start_web_repl",
            "Avbryt": "",
        },
        "enabled": True,
    },
    2: {
        "name": "2",
        "led_out": 16,
        "commands": {
            "Sound on<img>low_volume": "sound_on",
            "Sound off<img>high_volume": "sound_off",
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
        "commands": OrderedDict(
            [
                ("Alarm<img>alarm", "alarm"),
                ("Smyg pa<img>light_bulb_off", "light_bulb_off"),
                ("Smyg av<img>light_bulb_on", "light_bulb_on"),
                ("Starta repl<img>poop", "func:start_web_repl"),
            ]
        ),
        "enabled": True,
    },
    25: {"name": "2", "led_out": 19, "commands": {}, "enabled": False},
    33: {
        "name": "3",
        "led_out": 17,
        "commands": OrderedDict(
            [
                ("Barn TV<img>tv", "children_tv"),
                ("TV4<img>tv", "tv4"),
                ("Fire<img>heart", "fire"),
                ("Party<img>party", "party"),
            ]
        ),
        "enabled": True,
    },
    32: {
        "name": "4",
        "led_out": 27,
        "commands": OrderedDict([("Knapp 4", "button4_led_always_on")]),
        "enabled": True,
    },
    35: {"name": "5-not-working", "led_out": 2, "commands": {}, "enabled": False},
    34: {
        "name": "6",
        "led_out": 18,
        "commands": OrderedDict(
            [
                ("Ljus av<img>light_bulb_off", "lights_off"),
                ("Ljus pa<img>light_bulb_on", "lights_on"),
            ]
        ),
        "enabled": True,
    },
    39: {
        "name": "7",
        "led_out": 23,
        "commands": OrderedDict(
            [
                ("Allt av<img>all_off", "all_off"),
                ("Lag volym<img>low_volume", "low_volume"),
                ("Mellan vol<img>medium_volume", "medium_volume"),
                ("Hog vol<img>high_volume", "high_volume"),
                ("Grupp ljud<img>speaker", "group_audio"),
                ("Separat ljud<img>speaker", "ungroup_audio"),
            ]
        ),
        "enabled": True,
    },
}


mqtt_user = "homeassistant"
mqtt_pass = "snabel123!"
ssid = "EDOWIFI"
wifi_pw = "FEDCBAAAAA"
client_id = "my_buttons"
