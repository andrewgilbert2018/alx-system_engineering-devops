#A scrpt that remove limit of a domain name
exec { 'fix--reads-holbertonuser':
  path     =>  '/usr/bin:/usr/sbin:/bin',
  provider =>  shell,
  command  =>  'sed -i \'/holberton/c\\\' /etc/security/limits.conf'
}
