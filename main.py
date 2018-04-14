"""
ISTRUZIONI:

1. Indicare sensori e attuatori nel file config.json in configuration
2. Indicare ID App Engine nel file app_ening_id.dat in configuration
3. Nel caso, indicare sensori collegati all'adc, nel file sensChannel.json in configuration

4. Eseguire la prima volta la registrazione come indicato qui sotto:



from hal.communication.rest.registration import Registration

registr = Registration()
registr.sendConfig()


5. Una volta creato il file reg.dat, eseguire il file main di seguito illustrato

6. Inserire, se non già inserito, il file main nel file relativo all'esecuzione all'avvio del Raspberry

"""

from hal.communication.device.mqttManager import *

# avvio del client MQTT per il subscribe nel topic <app_engine_id>
url_broker = 'tools.lysis-iot.com'
client = createClient("Raspberry", url_broker)