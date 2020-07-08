# debbug
file { '/var/www/html/wp-settings.php':
  ensure => present,
}
-> exec { 'sed file':
  command => 'sed -i \'s/class-wp-locale.phpp/class-wp-locale.php/\' wp-setting\
s.php; sudo /etc/init.d/apache2 restart',
  cwd     => '/var/www/html',
  path    => ['/bin/', '/usr/sbin/'],
}
