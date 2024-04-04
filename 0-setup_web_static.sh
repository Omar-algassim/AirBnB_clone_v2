#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static.
sudo apt update
sudo apt-get -y nginx
# create dirctory
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
# creat inex.html with test text
sudo echo "Hello World" > /data/web_static/releases/test/index.html
# make a symbolink
ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu /data
chgrp -R ubuntu /data
# configure the nginx
str='location /hbnb_static{\n\talias /data/web_static/current/}'
sed -i "/listen [::]:80 default_server;/a $str/" /etc/nginx/sites-available/default
#check if there is any error
sudo nginx -t
# restart nginx
sudo service nginx restart
