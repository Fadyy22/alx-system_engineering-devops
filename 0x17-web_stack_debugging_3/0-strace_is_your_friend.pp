# Script that fixes 500 apache error

exec { 'fix_apache2':
    provider => shell,
    exec     => sed -i 's/phpp/php/g' /var/www/html/wp-settings.php
}
