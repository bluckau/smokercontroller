#!/usr/bin/env python
import time
import Stubs.RPi.GPIO as GPIO
import Adafruit_MAX31855.MAX31855 as MAX31855
import Adafruit_GPIO.SPI as SPI

FC=20
PWM=21
Magic = 1

THRESHOLD = 225
SWING = 1

METRIC=False
MODE=0 #0 is cool 1 is heat
INTERVAL = 5


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(FC, GPIO.OUT)


#HARDWARE SPI
SPI_PORT = 0
SPI_DEVICE = 0
sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=5000000))

def turn_on():
    print("Turn On!")
    GPIO.output(18, GPIO.HIGH)

def turn_off():
    GPIO.output(18, GPIO.LOW)
    print("Turn Off!")


def c_to_f(c):
    return c * 9.0/5.0 + 32.0

def main():
    #Main execution block

    while True:

        temp = sensor.readTempC()
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
            if (float(temp) < THRESHOLD) - SWING:
                turn_on()
            elif float(temp) > THRESHOLD + SWING:
                turn_off()

        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
