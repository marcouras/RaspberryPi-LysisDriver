import os

def write_file(filename, string):
    """
    :param filename: percorso del file che si vuole aprire
    :param string: stringa da inserire nel file
    :return: nessun dato restituito
    Nota: se il file non esiste viene creato, se invece esiste viene sovrascritto. Allo stato attuale non viene
    fatto nessun controllo sull'esistenza del file.
    """
    # path
    path = os.getcwd()
    # remove util from path
    path.replace('util', '')
    # completely filename
    filename = path + filename
    myfile = open(filename, mode='w+')
    myfile.write(string)
    myfile.close()


def read_file(filename):
    """
    :param filename: file da leggere
    :return: la prima riga del file in ingresso
    """
    try:
        # path
        path = os.getcwd()
        # remove util from path
        path.replace('util','')
        # completely filename
        filename = path + filename
        myfile = open(filename, mode='r')
        firstline = myfile.readline()
        myfile.close()
        return firstline
    except IOError:
        print (filename + " file not found")
