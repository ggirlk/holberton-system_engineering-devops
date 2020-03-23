
file { '/tmp/holberton':
   content => 'I love Puppet',
   mode => '0744',
   group => 'www-data',
}
