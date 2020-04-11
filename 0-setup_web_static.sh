#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "we are under construction" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
str='\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}'
sudo sed -i "38i $str" /etc/nginx/sites-available/default
nginx -s reload
exit 0
