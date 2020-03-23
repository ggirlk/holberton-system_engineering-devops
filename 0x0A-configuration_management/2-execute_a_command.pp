# Execute a command
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/local/bin/:/bin/',
}
