#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hal.communication.device.mqttManager import *
from hal.communication.rest.registration import Registration
from hal.communication.rest.sendData import sendData
from util.file_manager import createKey, project_path
import os


# check registration
if not (os.path.isfile('reg.dat')):
    key = createKey(10)
    f = open(project_path() + '/reg.dat', 'r')
    key = f.readline()
    st = Registration().sendConfig(key)
    if st == 200:
        print "Registration success!"
        # avvio del client MQTT per il subscribe nel topic <app_engine_id>
        url_broker = 'tools.lysis-iot.com'
        client = createClient("Raspberry", url_broker)
    else:
        print "Something went wrong..."
else:
    # avvio del client MQTT per il subscribe nel topic <app_engine_id>
    url_broker = 'tools.lysis-iot.com'
    client = createClient("Raspberry", url_broker)
    sen_name = 'TEMPERATURE'
    v = 10
    sendData(sensor_name=sen_name,sensor_value=v)

