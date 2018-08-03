from hal.communication.device.mqttManager import *

# attraverso tale test e' possibile testare i vari comandi inviati dal VO, quali GET, SET e SCHEDULE
# che devono essere pubblicati dal VO o, come test, dal file di test publish_mqtt

url_broker = 'tools.lysis-iot.com'

cliente = createClient("TEST", url_broker)

