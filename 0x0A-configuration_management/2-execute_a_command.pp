# kills a process named killmenow.
exec { 'name':
    command  => '/usr/bin/pkill killmenow'
}
