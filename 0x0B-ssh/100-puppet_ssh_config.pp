# a script that append to a line if
file_line { 'Turn off passwd auth':
ensure => 'present',
path   => '/etc/ssh/ssh_config',
line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
ensure => 'present',
path   => '/etc/ssh/ssh_config',
line   => 'IdentityFile ~/.ssh/school',
}
