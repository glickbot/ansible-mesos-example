#!/bin/bash

echo $@ >> update_nginx.log

cat << SHIM > /opt/shim/shims$1.conf
     location ~* /service$1 {
        rewrite /service$1/(.*) /\$1 break;
        proxy_pass http://$2:$3;
     }
SHIM

service nginx restart
