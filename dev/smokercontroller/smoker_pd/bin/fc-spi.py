#!/usr/bin/env python
import os
import glob
import time
import RPi.GPIO as GPIO
import Adafruit_MAX31855.MAX31855 as MAX31855
import Adafruit_GPIO.SPI as SPI

#TODO: to be replaced by a sensor object.


THRESHOLD = 300
SWING = 1

METRIC=False

MODE=1 #0 is cool 1 is heat
INTERVAL = 5


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(20,GPIO.OUT) # power to fan and led indicator
GPIO.setup(23,GPIO.OUT) # pwm fan control
GPIO.setup(24,GPIO.IN)

#HARDWARE SPI
SPI_PORT = 0
SPI_DEVICE = 0
sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=5000000))

def turn_on():
    print("Turn On!")
    GPIO.output(20,GPIO.HIGH)

def turn_off():
    GPIO.output(20,GPIO.LOW)
    print("Turn Off!")


def c_to_f(c):
    print("c is: ")
    print (c)
    return c * 9.0/5.0 + 32.0

def main():
    #Main execution block

    while True:

        temp = sensor.readTempC()
        print ("temp is: ")
        print (temp)
        ftemp = c_to_f(temp)

        print(ftemp)

        #COOLING
        if (MODE == 0):
            if float(temp) > THRESHOLD + SWING:
                turn_on()
            elif float(temp) < THRESHOLD - SWING:
                turn_off()
        
        #HEATING                
        if (MODE == 1):
            print("heating mode")
            if float(temp) < THRESHOLD:
                turn_on()
                print("on")
            else:
                turn_off()
                print("off")

            #if (float(temp) < THRESHOLD) - SWING:
            #    turn_on()
            #elif float(temp) > THRESHOLD + SWING:
            #    turn_off()
            #else:
            #    print("do nothing")

        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
