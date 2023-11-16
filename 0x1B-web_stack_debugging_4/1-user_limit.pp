# Puppet script that increases holberton user file open limit
exec { 'increase Hn':
    provider => shell,
    command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 1024/" /etc/security/limits.conf'
}

exec { 'increase Sn':
    provider => shell,
    command  => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 1024/" /etc/security/limits.conf'
}
