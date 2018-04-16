__author__ = "Claudio Marche"

from dataHandler.led.led import Led
from dataHandler.lirc.lirc import Lirc

# set command in actuators

def setActuator(actuator, command):

    if actuator == "LED":
        led = Led()
        if command == "GREEN-ON":
            led.red_off()
            led.green_lamp()
            led.green_on()
        elif command == "RED-ON":
            led.green_off()
            led.red_on()

    elif actuator == "IR":
        # esempio comando
        # HEAT-3-1 , dove il 3 sta per FAN e l'1 per VANE
        mode, fan, vane = command.split("-")
        lirc = Lirc()
        lirc.send(mode, fan, vane)