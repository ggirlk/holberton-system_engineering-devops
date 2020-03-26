# Client configuration file 
exec { 'ssh1':
  command  => 'echo IdentityFile ~/.ssh/holberton >> /etc/ssh/ssh_config',
  provider => shell,
}

exec { 'ssh2':
  command  => 'echo PasswordAuthentification no >> /etc/ssh/ssh_config',
  provider => shell,
}
