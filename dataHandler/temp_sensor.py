import Adafruit_DHT as dht

# classe per il sensore di temperatura interna

class Intern_sensor():

    def temp(self):
        h,t = dht.read_retry(dht.DHT22,4)
        return t

    def hum(self):
        h,t = dht.read_retry(dht.DHT22,4)
        return h
