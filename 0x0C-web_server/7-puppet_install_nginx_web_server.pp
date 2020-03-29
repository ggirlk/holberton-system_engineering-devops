#!/usr/bin/env bash
# Install Nginx web server (w/ Puppet)
exec { 'sudo apt-get -y update':
  provider => 'shell',
}
exec { 'sudo apt-get -y install':
  provider => 'shell',
}
exec { 'sudo apt install curl gnupg2 ca-certificates lsb-release':
  provider => 'shell',
}
exec { 'sudo apt-get -y upgrade':
  provider => 'shell',
}
exec { 'sudo apt-get -y install nginx':
  provider => 'shell',
}
exec { 'sudo service nginx start':
  provider => 'shell',
}
exec { 'sudo chmod 777 /var/www/html/index.nginx-debian.html':
  provider => 'shell',
}
exec { 'echo "Holberton School" | sudo cat > /var/www/html/index.nginx-debian.html':
  provider => 'shell',
}
exec { 'sudo ufw allow 'Nginx HTTP'':
  provider => 'shell',
}
exec { 'sudo chmod 777 /etc/nginx/sites-enabled/default':
  provider => 'shell',
}
exec { 'sudo sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default':
  provider => 'shell',
}
exec { 'sudo service nginx restart':
  provider => 'shell',
}
exec { 'sudo service nginx reload':
  provider => 'shell',
}
