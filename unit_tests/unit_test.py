import unittest
from configuration.configs import Pins
class UnitTests(unittest.TestCase):

    def test_get_setting_from_ini(self):
        fan0_pwr = Pins.get_pin("fan0_pwr")
        assert fan0_pwr == 20

