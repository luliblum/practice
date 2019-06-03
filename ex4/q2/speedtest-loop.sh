#!/bin/bash

log_file=speedtest.log

echo "#date, time,    download,    upload" > $log_file
#loop here

down_speed=$(speedtest-cli |grep -i "download:" | awk '{print $2}')

up_speed=$(speedtest-cli | grep -i "upload:" | awk '{print $2}')

current_time=$(date +'%d.%m.%Y.%H:%M:%S')
echo "$current_time,$down_speed,$up_speed" >> $log_file

