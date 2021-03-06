#!/usr/bin/python3
from Stubs import wiringpi as wiringpi

wiringpi.pwmSetMode(0) # PWM_MODE_MS = 0
wiringpi.wiringPiSetupGpio()  
wiringpi.pinMode(18, 2)      # pwm only works on GPIO port 18 out of the box 

wiringpi.pwmSetClock(6)  # this parameters correspond to 25kHz
wiringpi.pwmSetRange(1024)


def set_fan_speed(speed):
    print("set fan speed to:" + speed)
    wiringpi.pwmWrite(18, speed)

