# script that sets up web servers for deployment

$nginx_conf_file =  "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

exec {'update':
  provider => shell,
  command  => 'sudo apt -y update',
  before   => Exec['install nginx'],
}

exec {'install nginx':
  provider => shell,
  command  => 'sudo apt install -y nginx',
  before   => Exec['start nginx'],
}

exec {'start nginx':
  provider => shell,
  command  => 'sudo service nginx start',
  before   => Exec['test directory'],
}

exec {'test directory':
  provider => shell,
  command  => 'mkdir -p /data/web_static/releases/test/',
  before   => Exec['shared directory'],
}

exec {'shared directory':
  provider => shell,
  command  => 'mkdir -p /data/web_static/shared/',
  before   => Exec['fake html'],
}

exec {'fake html':
  provider => shell,
  command  => 'echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html',
  before   => Exec['ln link'],
}

exec {'ln link':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before   => File['/etc/nginx/sites-available/default'],
}

file {'/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf_file,
  before  => Exec['restart nginx'],
}

exec {'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
  before   => File['/data/'],
}

file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}
