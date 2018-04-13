import paho.mqtt.client as mqtt
from deviceMngt.schedule_thread import ThreadRasp
from deviceMngt.data_sensor import sendSensorData
from deviceMngt.set_actuator import setActuator


def createClient(Clientname):
    print "Hai collegato " + Clientname
    Clientname = mqtt.Client()
    Clientname.on_connect = on_connect
    Clientname.on_message = on_message
    Clientname.connect('http://lysis-78.appspot.com/sendData')
    Clientname.loop_forever()  # Continua a ricevere all'infinito

# Connessione device al Server
def on_connect(Clientname, userdata, flags, rc):
    print 'connected with result code ' + str(rc) + "\n"
    Clientname.subscribe('testMCLAB')  # Topic del progetto

# Ricezione messaggio dal server
def on_message(client, userdata, msg):
    print 'topic: ', msg.topic + '\nmessage: ' + str(msg.payload)

    # esempio payload
    # GET_TEMPERATURE
    payload = msg.payload.spli('_')

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




