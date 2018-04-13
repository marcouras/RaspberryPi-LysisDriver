from dataHandler.smartplug import SmartPlug
from dataHandler.temp_sensor import Intern_sensor
from hal.communication.rest.sendData import sendData

def sendSensorData(sensor_name):

    if sensor_name == "TEMPERATURE":
        dht = Intern_sensor()
        data = dht.temp()

    elif sensor_name == "HUMIDITY":
        dht = Intern_sensor()
        data = dht.hum()

    elif sensor_name == "POWER":
        smartplug = SmartPlug("192.168.1.1")
        data = smartplug.power()

    elif sensor_name == "CURRENT":
        smartplug = SmartPlug("192.168.1.1")
        data = smartplug.current()

    sendData(sensor_name, data)
