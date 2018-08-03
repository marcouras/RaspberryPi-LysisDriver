__author__ = "Marco Uras"

# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

# esempio di publish in broker mqtt

client = "TEST"
url_broker = ""
topic = ""
message = ""

mqttc = mqtt.Client(client, url_broker)
#mqttc.connect('test.mosquitto.org', 1883)
mqttc.connect(url_broker)
mqttc.publish(topic, message)
mqttc.loop(2) #timeout = 2s