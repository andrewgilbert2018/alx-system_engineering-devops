# a script that makes a command to be executed
exec {'killmenow':
command => 'pkill killmenow',
path    => '/usr/bin:/usr/sbin:/bin'
}
