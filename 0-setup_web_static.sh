#!/usr/bin/env bash
# set up web server for deployment

rule="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
file="/etc/nginx/sites-available/default"
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir "/data/web_static/shared/"
echo "ALX AFRICA!" > "/data/web_static/releases/test/index.html"
rm -f "/data/web_static/current"; ln -s "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -hR ubuntu:ubuntu "/data/"
sudo sed -i "38i\ $rule" "$file"
sudo service nginx restart
exit 0
