#!/bin/bash
wget https://github.com/ONSdigital/eq-submitter/archive/master.zip
unzip master.zip
mv eq-submitter-master eq-submitter
cd eq-submitter
sudo pip install -r requirements.txt
sudo service supervisor restart
