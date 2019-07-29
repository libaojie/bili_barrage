#!/bin/bash

function start_up()
{
	echo "启动服务"
	nohup main &
}

start_up
echo '@'$?

