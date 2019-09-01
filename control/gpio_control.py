#!/usr/bin/env python

import RPi.GPIO as GPIO
from configuration.configs import *

class GPIO_Control:
    def __init__(self, simulated:bool):
        self.simulated = simulated
        self.fan0_pwm = Pins.get_pin("fan0_pwm")
        self.fan0_pwr = Pins.get_pin("fan0_pwr")


    def turn_on(self):
        print("FAN ON")
        if self.simulated:
            self.write_fan('on")
        else:
            GPIO.output(self.fan0_pwr,GPIO.HIGH)

    def turn_off(self):
        print("FAN OFF")
        if self.simulated:
            self.write_fan("off")
        else:
            GPIO.output(self.fan0_pwr,GPIO.LOW)

    def setup(self):
        #Main execution block
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.fan0_pwr, GPIO.OUT)

    def write_fan(self, status):
        f = open(Config.get_sim_fan_pwr_file(), 'w+')
        f.write(status)
        f.close()

