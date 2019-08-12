#!/usr/bin/env python
from fanspeed import *
import os
import glob
import time
import RPi.GPIO as GPIO
THRESHOLD = 80
SWING = 5
MIN=0
MAX=1024
RANGE = MAX-MIN
FACTOR=1#about 10% for each 10 degrees diff

METRIC=False
MODE=1 #0 is cool 1 is heat
INTERVAL = 1
FAN = 20
LED1 = 19
LED2 = 13
LED3 = 6
LED4 = 5
BASE_DIR = '/sys/bus/w1/devices/'

device_folder = glob.glob(BASE_DIR + '3b*')[0]

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
    print("Turn On!")
    GPIO.output(FAN,GPIO.HIGH)
    GPIO.output(LED2,GPIO.HIGH)

def turn_off():
    print("Turn Off!")
    GPIO.output(FAN,GPIO.LOW)
    GPIO.output(LED2,GPIO.LOW)

def main():
    #Main execution block
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
  
    GPIO.setup(FAN,GPIO.OUT)
    GPIO.setup(LED2,GPIO.OUT)
    probe_modules()

    while True:
        speed = 0
        temp=read_temp()
        diff=THRESHOLD - temp
        if (diff > 0):
            speed = (RANGE/100) * diff * FACTOR
            #speed = 1024
            #print("speed = " + str(speed))
            if speed >= RANGE:
            
                set_fan_speed(MAX)
            else:
                set_fan_speed(int(speed))
        else:
            set_fan_speed(0)

        print("Temp:" + str(temp))
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
            if float(temp) < THRESHOLD - SWING:
                turn_on()
            elif float(temp) > THRESHOLD:
                turn_off()

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
