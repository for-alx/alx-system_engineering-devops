# Add a custom HTTP header with Puppet

exec { 'update':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
    ensure => 'installed',
    require => Exec['update']
}

file {'/var/www/html/index.html':
    content => 'Hello World!'
}

exec {'redirect':
    command => 'sed -i "24i\    rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
    provider => 'shell'
}

exec {'header':
    command => 'sed -i "25i\    add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
    provider => 'shell'
}

service {'nginx':
    ensure => running,
    require => Package['nginx']
}
