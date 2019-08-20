#!/usr/bin/env python3

from configparser import *
import os.path
default_config_file = "../etc/config_defaults.ini"




class Config:
    config = None

    @classmethod
    def load_config_file(cls, file = default_config_file):
        current_pwd = os.getcwd()
        print("Current pwd = {}".format(current_pwd))
        if not (os.path.exists(file) and os.path.isfile(file)):
            raise FileNotFoundError("file {} does not exist".format(file))
        cls.config = ConfigParser()
        cls.config.read(default_config_file)
        return cls.config

class Pins:
    config = Config.load_config_file()

    print(config['pins'])

    @classmethod
    def get_pin(cls, name):
        return cls.config['pins'].get(name)
