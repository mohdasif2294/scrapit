#!/bin/bash

sudo apt-get update

#sudo apt-get install build-essential
#sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
#cd ~/Downloads/
#wget http://python.org/ftp/python/2.7.5/Python-2.7.5.tgz
#tar -xvf Python-2.7.5.tgz
#cd Python-2.7.5
#./configure
#make
#sudo make install

sudo apt-get install python-pip
pip install requests
pip install beautifulsoup4

chmod +x scrap_geeks
cp scrap_geeks /bin/scrap_geeks

 
