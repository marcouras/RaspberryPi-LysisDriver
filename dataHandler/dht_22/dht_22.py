__author__ = "Claudio Marche"

import Adafruit_DHT as dht

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
