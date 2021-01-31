#!/bin/bash
echo "configing..."
sleep 250
echo "start poc.py"
echo "please wait...."
PYTHONIOENCODING=utf-8 python3 poc.py 
# web
#PYTHONIOENCODING=utf-8 python3 verify_config_success.py web
/usr/bin/tail -f /dev/null
