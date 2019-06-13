#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:

	print("Bad usage, expecting 1 argument")

else :

    dict_string={}

    word=sys.argv[1]

    for char in word:

        	dict_string[char]=word.find(char)

    print(dict_string)


