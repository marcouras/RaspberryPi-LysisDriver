import urllib
import requests
from util.file_manager import read_file

# esempio di publish eseguito dal VO
# tramite una chiamata post ad un noto server preconfigurato,
# il VO esegue un publish nel topic equivalente all'ID app engine

mqtt_bridge_url = 'tools.lysis-iot.com'
topic = read_file("../configuration/app_engine_id.dat")

message = "GET_TEMPERATURE"

#message = 'SET_IR_HEAT_1_2'
#message = 'SCHEDULE_HUMIDITY_60'

def mqtt_publish():
    form_data = urllib.urlencode(
        {'topic': topic, 'message': 'TEST'})

    result = requests.post(
        url=mqtt_bridge_url,
        data=form_data)
    return result.status_code


status_code = mqtt_publish()
print status_code
