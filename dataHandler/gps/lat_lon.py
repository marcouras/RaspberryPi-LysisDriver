__author__ = "Marco Uras"

import serial
import pynmea2
import time


def my_lat_lon_now():

        def set_gpgga(boolean_val):
            global gpgga  # Needed to modify global copy of globvar
            gpgga = boolean_val

        def print_gpgga():
            print(gpgga)  # No need for global declaration to read value of globvar

        def parseGPS(str):

            def edit_lat_lon(lat, lon):
                try:
                    merd = lat[:2]
                    angle = lat[2:]
                    merdff = merd
                    angleff = angle
                    merdff = float(merdff)
                    angleff = float(angleff)
                    angleff = angleff / 60
                    merdlon = lon[1:3]
                    anglelon = lon[3:]
                    merdfflon = merdlon
                    anglefflon = anglelon
                    merdfflon = float(merdfflon)
                    anglefflon = float(anglefflon)
                    anglefflon = anglefflon / 60
                    dict = {'lat': merdff + angleff, 'lon': merdfflon + anglefflon}
                    print_gpgga()
                    return dict

                except Exception:
                        dict = {'lat':0,'lon':0}
                        return dict

            if str.find('GGA') > 0:
                try:
                    msg = pynmea2.parse(str)

                except Exception:
                    msg.lat = None
                    msg.lon = None


                lat = msg.lat
                #at_dir = msg.lat_dir
                lon = msg.lon
                #lon_dir = msg.lon_dir
                if msg.lat is None:
                    return None
                    pass


                position = edit_lat_lon(lat=lat, lon=lon)

                print position
                # print "Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s" % (msg.timestamp,msg.lat,msg.lat_dir,msg.lon,msg.lon_dir,msg.altitude,msg.altitude_units)
                return position

        serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
        set_gpgga(True)
        while gpgga is True:
            str = serialPort.readline()
            position_dict = parseGPS(str)
            set_gpgga(False)
            time.sleep(1)
        return position_dict

def check_gps_fix():
    position = my_lat_lon_now()

    if position is None:
        return False
    else:
        return True

