#  Description:

A REST API call quary for MAC-address over the network in  https://macaddress.io/  and gets response of company name associated with that MAC address through docker container.

#  Pre-requesties:

Python 2.7

Docker

git


#  Installation of python :

# Python Pre-requesties

sudo apt-get update
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

# Download Python using following command from python official site and follow the commands

cd /usr/src
sudo wget https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz
sudo tar xzf Python-2.7.16.tgz
cd Python-2.7.16
sudo ./configure --enable-optimizations
sudo make altinstall
python2.7 -V
