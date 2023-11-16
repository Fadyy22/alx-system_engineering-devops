# Puppet script that increases the limit of reading files
exec { 'increase':
    provider => shell,
    command  => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx; service nginx restart'
}
