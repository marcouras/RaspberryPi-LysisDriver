__author__ = "Marco Uras"

import serial, time
import numpy as np
import json

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


def read_adc():
    # Software SPI configuration:
    CLK  = 18
    MISO = 23
    MOSI = 24
    CS   = 25

    channels = 2
    samples = 150  # change number of samples
    mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)


    # initialization of data array
    values = np.zeros(shape=(channels,samples));

    for ch in range(channels):
        for val in range(samples):
            #read value from adc channel
            values[ch , val] = mcp.read_adc(ch)


    print(values)
    return values


def get_channel(sensorName):
    with open('configuration/sensChannel.json') as data_file:
        conf = json.load(data_file)
    print(conf)
    sens_channels = dict(conf)
    return sens_channels.get(sensorName)


def read_sens(sensorName):

    matrix_values = read_adc()

    print sensorName
    ch = get_channel(sensorName)
    print ch
    mean = np.mean(matrix_values[ch-1])

    return mean