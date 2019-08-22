import unittest

def c_to_f(temp_c):
    temp_f = temp_c * (9.0 / 5.0) + 32.0
    return temp_f

def f_to_c(temp_f):
    temp_c = (temp_f - 32) / (9.0 / 5.0)
    return temp_c

class testUtilities(unittest.TestCase):

    def test_conversions(self):
        self.assertAlmostEqual(c_to_f(0), 32.0)
        self.assertAlmostEqual(c_to_f(-56), -68.8)
        self.assertAlmostEqual(c_to_f(67.33), 153.194)
        self.assertAlmostEqual(f_to_c(32), 0.0)
        self.assertAlmostEqual(f_to_c(-56),-48.88888889)
        self.assertAlmostEqual(f_to_c(67.33), 19.627777778)

