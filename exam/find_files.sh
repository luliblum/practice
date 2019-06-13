#!/bin/bash
#echo "Start!"

#while read p; do
#  echo "$p"
#done <text.txt


for word in $(cat text.txt); do echo $word; done
echo $word
