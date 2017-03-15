#!/usr/bin/env bash
# this sets up web servers for deployment
sudo apt-get update
sudo apt-get install -y nginx
sudo apt-get install -y curl
sudo mkdir -p /data/web_static/releases/test/index.html
sudo mkdir -p /data/web_static/shared/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "37i \tlocation /hbnb_static {\n\talias\t/data/web_static/current/;\n\t\tautoindex off;\n\t}\n" /etc/nginx/sites-enabled/default
echo "Holberton" | sudo tee /data/web_static/releases/test/index.html
sudo service nginx restart
