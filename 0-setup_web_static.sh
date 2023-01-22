#!/usr/bin/env bash
# Configured nginx server for custom header
sudo pkill -f nginx & wait $!

#check if ngix is installed
dpkg -s nginx &> /dev/null
if [ $? -ne 0 ]  
then                                                                                              
    sudo apt-get -y install nginx
fi
[ -d /data/web_static/release/test/ ] || sudo mkdir -p /data/web_static/releases/test/
[ -d /data/web_static/release/shared ] || sudo mkdir -p /data/web_static/shared/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
FILE=/etc/nginx/sites-available/default
REDIRECT_STRING="location /hbnb_static {\n alias /data/web_static/current; \n}\n"
sudo sed -i "39i $REDIRECT_STRING" $FILE
sudo service nginx restart
