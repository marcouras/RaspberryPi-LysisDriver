import os
import random, string


def createKey(length=10):
    key = ''.join(random.choice(string.lowercase) for i in range(length))

    write_file(filename=project_path() + '/reg.dat', string=key)
    return key


def project_path():
    # path
    path = os.getcwd()
    # remove util from path
    path.replace('util', '')
    return path


def write_file(filename, string):
    """
    :param filename: percorso del file che si vuole aprire
    :param string: stringa da inserire nel file
    :return: nessun dato restituito
    Nota: se il file non esiste viene creato, se invece esiste viene sovrascritto. Allo stato attuale non viene
    fatto nessun controllo sull'esistenza del file.
    """

    # completely filename
    filename = project_path() + filename
    myfile = open(filename, mode='w+')
    myfile.write(string)
    myfile.close()


def read_file(filename):
    """
    :param filename: file da leggere
    :return: la prima riga del file in ingresso
    """
    try:
        # completely filename
        filename = project_path() + filename
        myfile = open(filename, mode='r')
        firstline = myfile.readline()
        myfile.close()
        return firstline
    except IOError:
        print (filename + " file not found")


