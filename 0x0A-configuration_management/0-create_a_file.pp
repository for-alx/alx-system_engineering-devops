# This puppet script create a file called school containing "I love Puppetroot".
$content = "I love Puppet"
file { '/tmp/school':
  ensure  => 'present',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => $content,
}
