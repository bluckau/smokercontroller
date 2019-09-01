#!/usr/bin/env python3

import time

from control.probes import Probes
from control.gpio_control import GPIO_Control as Control
from configuration.configs import Config

class Controller:

    def __init__(self):
        simulated = Config.get_simulated()
        self.simulated = simulated
        self.control = Control(simulated)
        self.probe = Probes(simulated)
        self.threshold = Config.get_target_temp()

    def main(self):
        print("STARTING MAIN")
        #TODO: be able to start the simulator from here in a thread
        self.poison_pill = False
        while (self.poison_pill == False):
            temp = self.probe.read_temp()
            print("Temp: %s" % temp)
            print()

            trigger = False

            if float(temp) < self.threshold:
                self.control.turn_on()
            elif float(temp) >= self.threshold:
                self.control.turn_off()

            time.sleep(5)

if __name__ == "__main__":
    Controller().main()
