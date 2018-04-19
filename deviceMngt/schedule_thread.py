__author__ = "Claudio Marche"

from threading import Thread
import time
from data_sensor import sendSensorData

# Thread for scheduling

class ThreadRasp(Thread):

    def __init__(self, sensor, second):

        Thread.__init__(self)
        self.sensor = sensor
        self.val = second

    def run(self):
        while True:
            if self.val != 0:
                sendSensorData(self.sensor)
                print('%s data sent, next sample will be send in %d seconds...' % (self.getName(), self.val))
                time.sleep(self.val)
            else:
                break

    def stop(self):
        self.val = 0
