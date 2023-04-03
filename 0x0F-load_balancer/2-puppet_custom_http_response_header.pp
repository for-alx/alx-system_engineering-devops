# Add a custom HTTP header with Puppet

exec { 'apt update':
        command => '/usr/bin/apt-get update',
}
package { 'nginx':
    ensure  => 'installed',
    require => Exec['apt update']
}
file {'/var/www/html/index.nginx-debian.html':
    content => 'Hello World!'
}
file { 'Nginx configration':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
"server {
    # Robot added==============================
        location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

        error_page 404 /404.html;
        location = /404.html {
                root /var/www/html;
                internal;
        }
    # Add end======================================



    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    # Add index.php to the list if you are using PHP
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.

        # Robot added==================================
        add_header X-Served-By {hostname};
        # Add end======================================
        try_files \$uri \$uri/ =404;
    }
}",
}

service {'nginx':
    ensure  => running,
    require => Package['nginx']
}
