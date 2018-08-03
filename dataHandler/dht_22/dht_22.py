__author__ = "Claudio Marche"

import os
import pkgutil

# try to install DHT22 library
try:
    pkgutil.find_loader('Adafruit_DHT')
    import Adafruit_DHT as dht
except ImportError:
    os.system('sh install.sh')


# classe per il sensore DHT22

# h: humidity
# t: temperature

class Intern_sensor():

    def temp(self):
        h,t = dht.read_retry(dht.DHT22,4)
        return t

    def hum(self):
        h,t = dht.read_retry(dht.DHT22,4)
        return h
