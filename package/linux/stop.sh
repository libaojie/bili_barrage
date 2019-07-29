#!/bin/bash

function findpid()
{
	echo "查找pid"
        pid=`netstat -lntp | grep $1 | awk '{print $7}' | cut -d / -f1`
	if [ $? -eq 0 ];then 
		echo $pid
        	kill -9 $pid
	fi
}

findpid 15011
echo '@'$?

