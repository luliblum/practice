#!/bin/bash
#check args
function usage() {
        if [[ -z "$1" ]] ; then
                echo "The directory path is missing"
                echo "usage: [directory_path]"
                exit 1
        fi
} #usage

usage $1 

#extract passed args to readable vars
directory=$1


find $directory -type f | xargs -n1 -P0 md5sum | awk '{ print NR "," $2 "," $1}'

