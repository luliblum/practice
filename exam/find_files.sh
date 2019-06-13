#!/bin/bash
#echo "Start!"

#while read p; do
#  echo "$p"
#done <text.txt

#check args

function usage() {
        if [[ -z "$1" ]] || [[ -z "$2" ]]; then
                echo "You must enter the directory_path and the word to search"
		echo "One of the parameters is missing"
                echo "usage: [word to search] [directory_path]"
                exit 1
        fi
} #usage

usage $1, $2

#extract passed args to readable vars
word=$1
DIR=$2

#checking if the path_dir exists
if [[ -d $DIR ]]
	then
  		echo "The string '$word' find in this files:"
  		echo "-----------------------------------"
#recursivly search of word in files"
  		egrep -ril  $word $DIR   
#in case the path_dir doesn't exist
	else
  		echo "The path '$DIR' directory does not exists"
		echo "'$DIR' is not a valid directory"
fi




