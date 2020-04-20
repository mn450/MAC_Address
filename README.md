#  Description :

A REST API call quary for MAC-address over the network in  https://macaddress.io/  and gets response of company name associated with that MAC address through docker container.

#  Pre-requesties :

Python 2.7

Docker

git

API Key (sign up from  https://macaddress.io/ and get apikey)

----------------------------------------------------------------------------------------------------------------------------
#  Installation of Python :

#Python dependencies

sudo apt-get update

sudo apt-get install build-essential checkinstall

sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

#Download Python using following command from python official site and follow the commands

cd /usr/src

sudo wget https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz

sudo tar xzf Python-2.7.16.tgz

cd Python-2.7.16

sudo ./configure --enable-optimizations

sudo make altinstall

python2.7 -V

-----------------------------------------------------------------------------------------------------------------------------

# Installation of Docker :

apt-get update

sudo apt-get install \
apt-transport-https \
ca-certificates \
curl \
gnupg-agent \
software-properties-common -y

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

apt-get update

sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) \
stable"

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io -y

docker -v

# Installation of Git :

sudo apt install git

git --version

# Usage :

#Clone the MAC_address repository.

git clone https://github.com/mn450/MAC_Address.git

#Build the docker image by running below command

docker build -t macimage .

#Now run the container from macimage (docker image) by passing your apikey as environment and MAC-address as arguments

docker run -e apikeys="your api key" -ti macimage 3C-77-E6-EE-5F-98

#Finally you will get output of CompanyName with respect to MAC-address (3C-77-E6-EE-5F-98).

Company Name == Liteon Tech Corp
