# Execute a command
exec { 'refresh_cache':
  command => 'pkill ./killmenow',
  path    => '/usr/local/bin/:/bin/',
}
