from enum import Enum
from control.utils import *
from configuration.configs import *
import time
import random

class Unit(Enum):
    CELCIUS = 1
    FAHRENHEIT = 2

class Simulator():
    def __init__(self):
        self.temp_file_name = Config.get_sim_temp_file_name()
        self.fan_pwm_file = Config.get_sim_fan_pwr_file()
        self.fan_pwm_file = Config.get_sim_fan_pwm_file()
        self.wind = 5
        self.ambient_temp = 72
        self.ambient_temp = 72
        self.humidity = 50
        self.pit_temp = 72
        self.fuel = 10
        self.poison_pill = False

    def get_fan_speed(self):
        f = open(self.fan_pwm_file)
        return f.read()

    def write_temp(self, temp, unit = Unit.FAHRENHEIT):
        template = "31 00 4b 46 ff ff 05 10 1c : crc=1c YES\n31 00 4b 46 ff ff 05 10 1c t={}"

        if unit == Unit.FAHRENHEIT:
            converted_temp = f_to_c(temp)
        else:
            converted_temp = temp

        f = open(self.file_name, "w+")
        #write the template string with the {} replaced by the converted temperature.
        f.write(template.format(converted_temp))

    def main_loop(self):

        self.interval = Config.get_interval()

        while not self.poison_pill:
            self.do_it()
            time.sleep(self.interval)

    def randomize_wind(self):
        if random.randint(1, 100) > 90:
            self.wind = random.randint(1, 30)
            print ("changed wind to {}".format(self.wind))


    def randomize_ambient(self):
        MAX = 110
        MIN = 0

        num = random.randint(1, 100)
        if num > 80:
            if num < MAX: self.ambient = self.ambient + 1
        elif num > 60:
            if num > MIN: self.ambient = self.ambient - 1
        elif num  > 55:
            # one step back toward 72
            # we want to give it a slight proclivity to migrating back to 72
            if self.ambient > 72:
                self.ambient -= 1
            if self.ambient < 72:
                self.ambient +- 1


    def do_it(self):
        self.randomize_wind()
        self.fuel = self.fuel - 0.1
        if self.fuel > 4:
            change = (3 / self.pit_temp * 100)
        else:
            change = -1

        print ("Change = {}".format(change))

        self.pit_temp = self.pit_temp + change
        if self.pit_temp == self.ambient_temp:
            print ("pit_temp went out")
            self.poison_pill = True

        self.cook_temp = (self.ambient_temp + self.ambient_temp - self.wind + self.pit_temp) / 3

        print("pit_temp: {}".format(self.pit_temp))
        print("cook_temp: {}\n".format(self.cook_temp))
        f = open(self.temp_file_name, "w")
        f.write(str(self.cook_temp))
        f.close()

        if self.fuel < 2:
            #refuel
            self.fuel = 10

    @staticmethod
    def main():
        sim = Simulator()
        sim.main_loop()

if __name__ == "__main__":
    Simulator.main()
