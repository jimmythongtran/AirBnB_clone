#!/usr/bin/env bash
# this sets up web servers for deployment
sudo mkdir -p /data/web_static/releases/test/index.html
sudo mkdir -p /data/web_static/shared/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "4i location {\n\talias\t/data/web_static/current/;\n}" /etc/nginx/nginx.conf
echo "Holberton" > /data/web_static/releases/test/index.html
sudo service nginx restart
