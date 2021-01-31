#!/bin/bash
sleep 3
config_result=`docker logs config`

echo $config_result

[[ $config_result =~ "config success!" ]] || exit -1