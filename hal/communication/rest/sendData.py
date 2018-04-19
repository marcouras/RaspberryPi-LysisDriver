__author__ = "Marco Uras"

import urllib

import requests
import time
from util.file_manager import read_file
import os


def sendData(sensor_name, sensor_value):
    """
    Invio dei dati provenienti dai sensori al SVO

    """
    # path
    path = os.getcwd()

    try:
        f = open(path + 'reg.dat', 'r')
        key = f.readline()

    except IOError:
        print ("reg.dat file not found")


    payload = {'name': sensor_name,
               'type': 'number',
               'value': sensor_value,
               'regId': key,
               'timestamp': time.time()
               }

    param = urllib.urlencode(payload)
    url = "http://" + read_file("/configuration/app_engine_id.dat") + ".appspot.com/sendData"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
    }

    r = requests.request("POST", url=url, data=param,
                         headers=headers)
    print(r.text)
    print (r.status_code)


