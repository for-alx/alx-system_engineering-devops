# Client configuration file (w/ Puppet)
# Resource: 
# setup client SSH configuration

exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
        path    => '/bin/'
}
