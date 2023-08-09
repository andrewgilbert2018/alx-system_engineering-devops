# A script that fix a faulty web server
exec { 'replace_wrong':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  path    =>  '/bin:/usr/bin:/sbin:/usr/sbin:...'
}
