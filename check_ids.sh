#!/bin/bash
sleep 3
ids_result=`docker logs ids`

echo $ids_result

[[ $ids_result =~ "detect rce attack" ]] || exit -1