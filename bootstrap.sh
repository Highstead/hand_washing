#!/usr/bin/env bash

apt-get update
apt-get install -y apache2
rm -rf /var/www
ln -fs /vagrant /var/www

sudo apt-get install pip
sudo pip install /vagrant/requirements.txt -r