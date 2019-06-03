#!/bin/bash
#check args
function usage() {
	if [[ -z "$1" ]] || [[ -z "$2" ]]; then
		echo "Wrong number of passed args: Must pass an extension and a dir path!"
		exit 1
	fi
} #usage

usage $1, $2

#extract passed args to readable vars
extension=$1
dir=$2

if [[ $dir != */ ]]; then
	dir="$dir/"
fi

for entry in `ls $dir`; do
	if [[ $entry != *sh ]] && [[ $entry != *mp3 ]]; then
		`mv $dir$entry $dir$entry.$extension`
	fi
done

