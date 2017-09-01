from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import serial

class LightHandler(object):

    # def __init__(self, pin=None):
    #     # if not pin:
    #     #     self.pin = app.config['PIN']

    def get_pin(self):
        return self.pin

    def set_pin(self, pin):
        try:
            self.pin = pin
            return True
        except Exception as exc:
            print "Failed to set pin: %s" % exc
            return False

    def on(self, colour):
        print "Turning on custom light"
        self.turnLight(True, colour)

    def off(self):
        print "Turning light off"
        self.turnLight(False)

    def turnLight(self, signal, colour = None):
        return True
        # """
        # Controls the signal going to the specified pin. Accepts two arguments:
        # + pin: The number of the GPIO pin to receive the signal
        # + signal: Boolean (True or False) indicating whether there should be
        #           a current or not going to the specified pin.
        # """
        # try:
        #     GPIO.setmode(GPIO.BOARD)
        #     GPIO.setup(pin, GPIO.OUT)
        #     GPIO.output(pin, signal)
        #
        #     return signal
        #
        # except Exception as exc:
        #     print "Failed to control GPIO Pins: %s" % exc
        #     return not signal