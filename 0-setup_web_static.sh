#!/usr/bin/env bash
# install nginx and open folders

apt update

apt install -y nginx

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
printf %s "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>
" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

sed -i '11i\\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default

service nginx restart
exit 0
