import RPi.GPIO as GPIO
import time


GREEN = 5
RED = 6


class Led():

    # metodo per l'accensione del led verde
    def green_on(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)     # disabilita' warning
        GPIO.setup(GREEN, GPIO.OUT)
        GPIO.output(GREEN, GPIO.HIGH)


    # metodo spegnimento led verde
    def green_off(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)  # disabilita' warning
        GPIO.setup(GREEN, GPIO.OUT)
        GPIO.output(GREEN, GPIO.LOW)


    # metodo un lampeggi verde. Uno solo se non e' andata a buon fine, tre se e' andata a buon fine.
    def green_lamp(self, val):

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)  # disabilita' warning
        GPIO.setup(GREEN, GPIO.OUT)

        if val == True:
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
        else:
            GPIO.output(GREEN, GPIO.LOW)
            time.sleep(3)
            GPIO.output(GREEN, GPIO.HIGH)




    # metodo per l'accensione e lo spegnimento del led rosso
    def red_on(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)  # disabilita' warning
        GPIO.setup(RED, GPIO.OUT)
        GPIO.output(RED, GPIO.HIGH)



    # metodo spegnimento led verde
    def red_off(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)  # disabilita' warning
        GPIO.setup(RED, GPIO.OUT)
        GPIO.output(RED, GPIO.LOW)






