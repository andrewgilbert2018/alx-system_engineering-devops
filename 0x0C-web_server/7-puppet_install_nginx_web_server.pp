# a puppet script that install nginx
# Install
exec{ 'Install':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx && echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html && sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default-backup && redirect="\n\tserver_name bestameh.tech;\n\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" && sudo sed -i "37i\ $redirect" /etc/nginx/sites-available/default && sudo service nginx start',
  provider => shell,
}
