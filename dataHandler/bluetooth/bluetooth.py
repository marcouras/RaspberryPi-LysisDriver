__author__ = "Claudio Marche"

import subprocess

# classe per il bluetooth

class Bluetooth():

    def scan(self):

        p = subprocess.Popen(['hcitool','scan'], stdout=subprocess.PIPE)

        # lista di dispositivi bluetooth presenti vicino al raspberry
        mac_and_name = p.communicate()[0].split("/t")[1:]

        # estraggo solo i nomi
        users = []
        for i,element in mac_and_name:
            if i%2:
                new_len = len(element) - 1
                users.append(element[:new_len])

        return users



