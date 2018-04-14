__author__ = "Marco Uras"

from dataHandler.gps.lat_lon import *


def set_isfixed(boolean_val):
    global is_fixed  # Needed to modify global copy of globvar
    is_fixed = boolean_val


def print_isfixed():
    print(is_fixed)

gps_is_fixed = False


while not gps_is_fixed:
    print ("....Waiting for GPS.....")
    gps_is_fixed = check_gps_fix()
    time.sleep(1)