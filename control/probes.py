#!/usr/bin/env python

import os
import glob
import time
import RPi.GPIO as GPIO
from configuration.configs import *

BASE_DIR = '/sys/bus/w1/devices/'

class Probes:
    def __init__(self, simulated:bool):
        self.simulated = simulated
        # for the 1-wire interface:
        if (not simulated):
            device_folder = glob.glob(BASE_DIR + '28*')[0]
            self.device_file = device_folder + '/w1_slave'
            self.probe0 = Pins.get_pin("probe0")
            self.probe_modules()

    INTERVAL = Config.get_interval()

    def probe_modules(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

    def read_temp_raw(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        temp_c = 0
        if(self.simulated):
            with open(Config.get_sim_temp_file_name(), 'r') as myfile:
                data = myfile.read().strip()
                myfile.close()
                return float(data)

        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')

        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0

        return temp_c