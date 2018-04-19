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
        self.id_app_engine = read_file(project_path() + "/configuration/app_engine_id.dat")

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

        print param

        payload = urllib.urlencode(param)

        headers_list = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
        }

        r = requests.request("POST",
                             url="http://" + self.id_app_engine + ".appspot.com/register?device",
                             data=payload,
                             headers=headers_list)
        # print r.text
        print r.status_code
