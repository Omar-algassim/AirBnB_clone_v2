#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static.
sudo apt update
sudo apt-get -y install nginx
# create dirctory
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
# creat inex.html with test text
echo "Hello World" | sudo tee /data/web_static/releases/test/index.html
# make a symbolink
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu /data
sudo chgrp -R ubuntu /data
# configure the nginx
sudo sed -i '24i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default
#check if there is any error
sudo nginx -t
# restart nginx
sudo service nginx restart
