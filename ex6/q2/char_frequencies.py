#!/usr/bin/python3

import sys
import os


all_freq={}
if len(sys.argv) < 2:
    print ("the string to check is missing!!!")
    print ("usage: <string to check>")
    exit(0)
else:
    test_str=sys.argv[1]
    for i in test_str:
        if i in all_freq:
            all_freq[i] +=1
        else:
            all_freq[i]=1

print ("count of all characters in " +"'"+ test_str +"'" + " is :"+" \n"+ str(all_freq))

