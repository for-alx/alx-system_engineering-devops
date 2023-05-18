# Change the OS configuration limit

# hard limit OS configuration
exec { 'hard-limit':
  path    => '/bin',
  command => "sed -i 's/5/20500/' /etc/security/limits.conf"
}

# soft limit OS configuration
exec { 'soft-limit':
  path    => '/bin',
  command => "sed -i 's/4/20500/' /etc/security/limits.conf"
}
