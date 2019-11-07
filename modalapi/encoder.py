#!/usr/bin/env python3

import RPi.GPIO as GPIO

from functools import partial


class Encoder:

    def __init__(self, d_pin, clk_pin, callback):

        self.d_pin = d_pin
        self.clk_pin = clk_pin
        self.callback = callback
        self.lcd_refresh_required = False

        GPIO.setup(self.d_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.clk_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # bouncetime less than 400 causes a double trigger of the callback if the callback is slow (eg. preset change)
        GPIO.add_event_detect(self.clk_pin, GPIO.FALLING, callback=partial(self.callback, self), bouncetime=400)

    def get_data(self):
        return GPIO.input(self.d_pin)


