#!/bin/bash
sleep 3
poc_result=`docker logs poc`

echo $poc_result

[[ $poc_result =~ "PoC success!" ]] || exit -1