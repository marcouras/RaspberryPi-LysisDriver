Execute following commands

sudo apt-get update
sudo apt-get install build-essential python-dev python-openssl
sudo apt-get install git-core

###############################################################

For DHT22 sensor install

git clone https://github.com/adafruit/Adafruit_Python_DHT
cd Adafruit_Python_DHT
sudo python setup.py install

###############################################################

Set configurations in configuration package:

In configuration.json -> sensors and actuators in VO
In sensChannel.json   -> sensors connected to ADC MCP3008 (if it's present)
In app_engine.id.dat  -> ID App Engine (project ID)