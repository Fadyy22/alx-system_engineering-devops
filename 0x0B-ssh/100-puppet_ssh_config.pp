# edit ssh config file
exec { 'ssh config':
    path    => '/usr/bin',
    command => 'echo "\n    PasswordAuthentication no\n    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
}
