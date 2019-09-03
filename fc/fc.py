#!/usr/bin/env python

import os
import glob
import time
import Stubs.RPi.GPIO as GPIO
from fan_speed import *

THRESHOLD = 80
SWING = 1
PWM=18
FAN_PWR=20
PROBE=21

METRIC=False
MODE=0 #0 is cool 1 is heat
INTERVAL = 5
BASE_DIR = '/sys/bus/w1/devices/'

device_folder = glob.glob(BASE_DIR + '28*')[0]

#Currently only supporting 1 temp
device_file = device_folder + '/w1_slave'
def probe_modules():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
	
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')

    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0

        if METRIC == True:
            return temp_c
        else:
            return temp_f
	
def turn_on():
    GPIO.output(FANPWR, GPIO.HIGH)

def turn_off():
    GPIO.output(FANPWR, GPIO.LOW)

def main():
    #Main execution block
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(FANPWR, GPIO.OUT)

    probe_modules()

    while True:
        temp=read_temp()
        print("Temp: %s" % temp)
        print("")

        trigger = False

        #COOLING
        if (MODE == 0):
            if float(temp) > THRESHOLD + SWING:
                turn_on()
            elif float(temp) < THRESHOLD - SWING:
                turn_off()
        
        #HEATING                
        if (MODE == 1):
            if (float(temp) < THRESHOLD) - SWING:
                turn_on()
            elif float(temp) > THRESHOLD + SWING:
                turn_off()

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
