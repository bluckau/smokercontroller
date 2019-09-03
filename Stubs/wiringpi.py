# stub for compatibility on windows. this file should not be checked in to git in the normal place, but can be copied to the root of the project.
def pwmSetMode(mode):
    pass
def wiringPiSetupGpio():
    pass
def pinMode(pin, mode):    # pwm only works on GPIO port 18 out of the box
    pass
def pwmWrite(pin, speed):
    pass
def pwmSetClock(freq):  # this parameters correspond to 25kHz
    pass
def pwmSetRange(range):
    pass
