class createfile {
  file { '/tmp/holberton':
    ensure  => '/tmp/holberton',
    replace => 'no',
    content => 'I love Puppet',
    mode => '0744',
    group => 'www-data',
    owner => 'www-data',
  }
}