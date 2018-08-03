__author__ = "Marco Uras"

# -*- coding: utf-8 -*-
import simplejson as json
import urllib

from util.file_manager import *
import requests

from pprint import pprint



class Registration(object):
    """
    Questa classe si occupa di fare la registrazione del Raspberry sul SVO
    viene generata, spedita ed infine memorizzata una chiave
    """

    def __init__(self):
        self.id_app_engine = read_file("/configuration/app_engine_id.dat")

    def sendConfig(self, key):
        """
        risorsa da contattare
        http://svotest-002n.appspot.com/register?device
        :return:
        """

        # path
        path = project_path()

        with open(path + '/configuration/config.json') as data_file:
            conf = json.load(data_file)
            pprint(conf)


        param = {'brand': 'raspberryPi',
                 'model': '3',
                 'url': self.id_app_engine,
                 'regId': key,
                 'configuration': conf}

        payload = urllib.urlencode(param)
        print payload

        url = "http://" + self.id_app_engine + ".appspot.com/register?device"
        print url

        headers_list = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
        }

        r = requests.request("POST",
                             url=url,
                             data=payload,
                             headers=headers_list)
        # print r.text
        print r.status_code
        return r.status_code
