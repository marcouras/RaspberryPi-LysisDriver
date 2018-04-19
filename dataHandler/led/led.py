import RPi.GPIO as GPIO
import time

__author__ = "Claudio Marche"

# GPIO
GREEN = 12
RED = 6


class Led():

    # green led on
    def green_on(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)  # warning off
        GPIO.setup(GREEN, GPIO.OUT)
        GPIO.output(GREEN, GPIO.HIGH)


    # green led off
    def green_off(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)  # warning off
        GPIO.setup(GREEN, GPIO.OUT)
        GPIO.output(GREEN, GPIO.LOW)


    # green led blinking
    def green_lamp(self, val):

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)  # warning off
        GPIO.setup(GREEN, GPIO.OUT)

        if val == True: # if val = True, three blibk
            GPIO.output(GREEN, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(GREEN, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(GREEN, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(GREEN, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(GREEN, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(GREEN, GPIO.HIGH)
        else:           # if val = False, one blink
            GPIO.output(GREEN, GPIO.LOW)
            time.sleep(3)
            GPIO.output(GREEN, GPIO.HIGH)




    # red led on
    def red_on(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)  # warning off
        GPIO.setup(RED, GPIO.OUT)
        GPIO.output(RED, GPIO.HIGH)



    # red led off
    def red_off(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)  # warning off
        GPIO.setup(RED, GPIO.OUT)
        GPIO.output(RED, GPIO.LOW)






