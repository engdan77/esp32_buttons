from images import (
    poop,
    tv,
    party,
    light_bulb_on,
    light_bulb_off,
    alarm,
    speaker,
    all_off,
    medium_volume,
    low_volume,
    high_volume,
)
from ucollections import OrderedDict

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
            "Sound on<img>{}".format(low_volume): "sound_on",
            "Sound off<img>{}".format(high_volume): "sound_off",
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
                ("Alarm<img>{}".format(alarm), "alarm"),
                ("Starta repl<img>{}".format(poop), "func:start_web_repl"),
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
                ("Barn TV<img>{}".format(tv), "children_tv"),
                ("TV4<img>{}".format(tv), "tv4"),
                ("Fire<img>{}".format(tv), "fire"),
                ("Party<img>{}".format(party), "party"),
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
                ("Ljus pa<img>{}".format(light_bulb_off), "lights_off"),
                ("Ljus av<img>{}".format(light_bulb_on), "lights_on"),
            ]
        ),
        "enabled": True,
    },
    39: {
        "name": "7",
        "led_out": 23,
        "commands": OrderedDict(
            [
                ("Allt av<img>{}".format(all_off), "all_off"),
                ("Lag volym<img>{}".format(low_volume), "low_volume"),
                ("Mellan vol<img>{}".format(medium_volume), "medium_volume"),
                ("Hog vol<img>{}".format(high_volume), "high_volume"),
                ("Grupp ljud<img>{}".format(speaker), "group_audio"),
                ("Separat ljud<img>{}".format(speaker), "ungroup_audio"),
            ]
        ),
        "enabled": True,
    },
}


mqtt_user = "homeassistant"
mqtt_pass = "***REMOVED***"
ssid = "***REMOVED***"
wifi_pw = "***REMOVED***"
client_id = "my_buttons"
