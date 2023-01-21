#!/usr/bin/env bash
# Configured nginx server for custom header
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
FILE=/etc/nginx/sites-available/default
REDIRECT_STRING="location /hbnb_static {\n alias /data/web_static/current; \n}\n"
sudo sed -i "39i $REDIRECT_STRING" $FILE
sudo service nginx restart
