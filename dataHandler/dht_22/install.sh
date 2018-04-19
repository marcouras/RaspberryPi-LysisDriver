sudo apt-get update
sudo apt-get install build-essential python-dev python-openssl

sudo apt-get install git-core

cd /home/pi

git clone https://github.com/adafruit/Adafruit_Python_DHT

cd Adafruit_Python_DHT
sudo python setup.py install
