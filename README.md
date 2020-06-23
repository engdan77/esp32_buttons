# esp32_buttons

Since I've been doing home-automations and some clever integrations using [Home Assistant](https://www.home-assistant.io) I felt a need to bring out the soldering iron once more to build a battery-driven "button-board" that would have an OLED display and physical buttons that would allow one to chose different option using a single button. And this being integrated to MQTT to allow one easily configure the button actions from Home Assistant. And now since I needed the hardware to keep responsive even though it waking up from deep-sleep and establishing Wifi connection in parallell with "glowing led" and still allow the user to press the button and see the display being updated I had to use asyncrously-paradigm.

In this project I also took the oportunity to allow "mimic" the OLED using PySimpleGUI framework so that I easier could test the software in my MacOS.

## Installation

What you need to do is to basically update the config.py file

```bash
# buttons_conf_other (is for using PySimpleGUI)
# buttons_conf_esp32 used if you run from an ESP32

# The structure is
# main key (int): is the key or input-pin on ESP
# name (str): could be anything
# commands (dict): text w/o image-variable: display-text or function
# enabled (bool): enabled/disabled

# This would be used if you're not running on ESP
buttons_conf_other = {
    1: {
        "name": "1",
        "led_out": 16,
        "commands": {
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

# This is the config being used if you run from an ESP
buttons_conf_esp32 = {
    26: {
        "name": "1",
        "led_out": 16,
        "commands": OrderedDict(
            [
                ("Alarm<img>alarm", "alarm"),
                ("Light off<img>light_bulb_off", "light_bulb_off"),
                ("Starta repl<img>poop", "func:start_web_repl"),
            ]
        ),
        "enabled": True,
    }
}

# This is the configuration for the MQTT and Wifi
mqtt_user = "homeassistant"
mqtt_pass = "foo"
ssid = "MYWIFI"
wifi_pw = "bar"
client_id = "my_buttons"

```

Then obviously if an ESP32 you need to upload those files to the flash, otherwise you can run the main.py if you running on anything else.

#### Adding images to the display

If you'd like to include images to the output you can do so by suffixing the display-text with `<img>foo` where **foo** being the variable name that you import being a 40x40 1-dimensional matrix of 1/0 for the pixel on/off.

I highly suggest tool such like https://www.dcode.fr/binary-image to convert you image to a matrix before including this into **images.py**



## Image of the end result (ugly but working)

![esp32_buttons](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfy1mxqivlj30m80go7on.jpg)



## UML class diagram

![uncached image](http://www.plantuml.com/plantuml/png/TLJ1ZXCn3BtFL_G8Xrt1hiHXnM55kI2n1zIzHsdYjXOPPveuxOuG_qxYoPIC60vj_1oFtxETv3co3fnwrncdOzoyZ2y_NbytlxhDne4j_zuFUUdFpCeu1E8RydJ0OqRP833yxdss8GwF3whr36dlC9x4jXZRBOnp95XnA8M4h5G6lxkgw4jYzXH5qetoNAX8xul6zhCgM0t16uXH74VWZ3Eg9BqtFoU7mCX-QFbs9W2Gq4NZr81K-TuKmrkfllHZd45TJe374yi6zle82ttHwfhdYfPFackEyZL4L9Ja0Od5uXH8-SDXsHa15kFWTAMQNFATAjbQN6fTxufne4DRztUmKdGGFSVIXBpkNG8PeekWVF4S0fmJa1dBhiocr1Qd0wCOUmZn_zEHuwOatQtx2wXvihIjoGG5wFq56eTOgbJL3h4sJJjN6jTMj_N4mJi7GOhSvvz8BkTXeTOFZ9uAaq_SubgNII40iPfARnnJeCpuW18_9SZqS_Hy3BCNIHl62_8uXpQfcatZ4x7rLresSYs1T6DzsDDXq6JLLICtWv2oLgz1UGQsSjzpmxg__XZjnySFd-vtkwzbLTyUjii07KSowE_BjOCBqAHh6JFeaw-loVsIfA7zV7StFqTFZPnkJK69hHVtQKrYjwvgoR4UqxLYrwJzkzyz0zdKkpy0)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)