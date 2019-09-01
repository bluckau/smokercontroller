#!/usr/bin/env python3

from configparser import *
import os.path
default_config_file = "../etc/config_defaults.ini"

class Config:
    config = None

    @classmethod
    def get_target_temp(cls):
        return int(cls.config['tuning'].get('target_temp'))

    @classmethod
    def load_config_file(cls, file = default_config_file):
        current_pwd = os.getcwd()
        print("Current pwd = {}".format(current_pwd))
        if not (os.path.exists(file) and os.path.isfile(file)):
            raise FileNotFoundError("file {} does not exist".format(file))
        cls.config = ConfigParser()
        cls.config.read(default_config_file)
        return cls.config

    @classmethod
    def get_interval(cls):
        return int(cls.config['tuning'].get('interval'))

    @classmethod
    def get_simulated(cls):
        string = cls.config['sim'].get('simulated').strip().lower()
        return string == "true" or string == "1"

    @classmethod
    def get_sim_fan_pwr_file(cls):
        return cls.config['sim'].get('sim_fan_pwr_file')

    @classmethod
    def get_sim_temp_file_name(cls):
        return cls.config['sim'].get('sim_temp_file_name')

    @classmethod
    def get_sim_fan_pwm_file(cls):
        return cls.config['sim'].get('sim_fan_pwm_file')



class Pins:
    config = Config.load_config_file()

    print(config['pins'])

    @classmethod
    def get_pin(cls, name):
        return cls.config['pins'].get(name)