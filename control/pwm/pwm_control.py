#!/usr/bin/python3
import wiringpi as wiringpi
from configuration.configs import Pins

class PWMControl:

    def __init__(self):
        self.pwm0_pin = Pins.get_pin("pwm0")
        wiringpi.pwmSetMode(0) # PWM_MODE_MS = 0
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(self.pwm0_pin, 2)      # pwm only works on GPIO port 18 out of the box

        wiringpi.pwmSetClock(5)  # this parameters correspond to 25kHz
        wiringpi.pwmSetRange(1000)


    def set_fan_speed(self, speed):
        print("set fan speed to: " + str(speed))
        wiringpi.pwmWrite(self.pin, speed)