# install and configure nginx web server
exec { 'nginx':
    provider => shell,
    command  => 'sudo apt-get update; sudo apt-get install -y nginx; echo "Hello World!" > /var/www/html/index.nginx-debian.html; sudo ufw allow "Nginx HTTP"; sudo sed -i "s/server_name _;/server_name _;\n\tlocation \/redirect_me {\n\t\t return 301 http:\/\/google.com;\n\t}/" /etc/nginx/sites-available/default; sudo service nginx start;',
}
