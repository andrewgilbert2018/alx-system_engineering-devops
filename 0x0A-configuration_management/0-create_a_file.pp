# This manifesto creates a file called school
file {'/temp/school/':
ensure  => present,
path    => '/tmp/school',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}
