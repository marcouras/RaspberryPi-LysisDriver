__author__ = "Marco Uras, Claudio Marche"

import paho.mqtt.client as mqtt
from deviceMngt.schedule_thread import ThreadRasp
from deviceMngt.data_sensor import sendSensorData
from deviceMngt.set_actuator import setActuator
from util.file_manager import read_file


def createClient(Clientname, url_broker):
    print "Hai collegato " + Clientname
    Clientname = mqtt.Client()
    Clientname.on_connect = on_connect
    Clientname.on_message = on_message
    Clientname.connect(url_broker)
    Clientname.loop_forever()  # Continua a ricevere all'infinito

# Connessione device al Server
def on_connect(Clientname, userdata, flags, rc):
    print 'connected with result code ' + str(rc) + "\n"
    topic = read_file("/configuration/app_engine_id.dat")
    Clientname.subscribe(topic)  # Topic del progetto

# Ricezione messaggio dal server
def on_message(client, userdata, msg):
    print 'topic: ', msg.topic + '\nmessage: ' + str(msg.payload)

    # esempio payload
    # GET_TEMPERATURE
    payload = msg.payload.split('_')

    if payload[0] == "GET":
        sendSensorData(payload[1])

    elif payload[0] == "SET":
        setActuator(payload[1], payload[2])

    elif payload[0] == "SCHEDULE":
        if payload[2] != 0:    # se l'intervallo e' diverso da zero
            global thread
            thread = ThreadRasp(payload[1], payload[2])
            thread.start()
        elif payload[2] == 0:  # stop schedule
            thread.val = 0




