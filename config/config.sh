#!/bin/bash
STATUS=""
#while [ "$STATUS" != "200" ]
#do
#    sleep 5
#    STATUS=$(curl -sL -w "%{http_code}" http://web -o /dev/null)
#    STATUS=$(curl -sL -w "%{http_code}" http://192.168.56.101:8081 -o /dev/null)
#done
sleep 10
echo "start config.py"
echo "please wait for several minutes...."
PYTHONIOENCODING=utf-8 python3 config.py 
# web
#PYTHONIOENCODING=utf-8 python3 verify_config_success.py web
/usr/bin/tail -f /dev/null
