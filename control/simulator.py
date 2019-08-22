from enum import Enum
from control.utils import Utils
class Unit(Enum):
    Celsius = 1
    Fahrenheit = 2

class Simulator():

    def __init__(self, file_name = "/tmp/simulated_temp"):
        self.file_name = file_name

    def write_temp(self, temp, unit = Unit.Farenheit):
        template = "31 00 4b 46 ff ff 05 10 1c : crc=1c YES\n31 00 4b 46 ff ff 05 10 1c t={}"

        if (unit == Unit.Farenheit):
            converted_temp = Utils.f_to_c(temp)
        else
            converted_temp = temp

        f = open(self.file_name, "w+")
        f.write(template.format(converted_temp))

    def main(self):
        print "hello"

if __name__ == "__main__":
    Simulator.main()