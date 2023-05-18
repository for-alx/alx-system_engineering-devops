# change default nginx limit to 2000

exec { 'limit':
  path    => '/bin',
  command => "sed -i 's/15/2000/' /etc/default/nginx"
} ->

exec { 'restart nginx service':
  path    => '/etc/init.d/',
  command => 'nginx restart'
}
