#!/usr/bin/python3
import sys
from os import path
from sys import argv 

def grep(path, word):
    with open (file_name) as f:
        #line = f.readline()
        for line in f.readlines():
            #print ('DEBUG--\t%s' % line)
            if word in line:
                print (line)

print ("Arguments:")
print ("----------")
for arg in sys.argv:
    print (arg)  

print ("----------------------------------------------")
if __name__ == '__main__':
    if len(argv) != 3:
            print ("usage: <path_file> <word>")
        
            raise Exception ("Wrong number of arguments. Please provide two argumets: file path and word!")

    file_name, word = argv[1], argv[2]
    if not path.isfile(file_name):
            print ("usage: <path_file> <word>")
            raise Exception ("The provided path doesn't point to an existing path!")
    print ("")
    print ("")
    print ("Solution of the search:")
    print ("-----------------------")
    grep(file_name, word)
