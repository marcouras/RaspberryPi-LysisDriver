__author__ = "Claudio Marche"

from dataHandler.smartplug.smartplug import SmartPlug
from dataHandler.dht_22.dht_22 import Intern_sensor
from hal.communication.rest.sendData import sendData
from dataHandler.adc.read_values import *
from dataHandler.gps.lat_lon import *

# classe utilizzata per la lettura dei dati dai sensori, inviati tramite comunicazione rest descritta nel
# package communication


def sendSensorData(sensor_name):

    if sensor_name == "TEMPERATURE":
        dht = Intern_sensor()
        data = dht.temp()

    elif sensor_name == "HUMIDITY":
        dht = Intern_sensor()
        data = dht.hum()

    elif sensor_name == "POWER":
        smartplug = SmartPlug()
        data = smartplug.power()

    elif sensor_name == "CURRENT":
        smartplug = SmartPlug()
        data = smartplug.current()

    elif sensor_name == "SOUND" or sensor_name == "AIRQ":
        data = read_sens(sensor_name)

    elif sensor_name == "POSITION":
        data = my_lat_lon_now()

    # invio dati
    sendData(sensor_name, data)
