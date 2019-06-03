#!/usr/bin/python3

from os import path
from sys import argv 

def grep(path, word):
    with open (file_name) as f:
        #line = f.readline()
        for line in f.readlines():
            #print ('DEBUG--\t%s' % line)
            if word in line:
                print (line)


if __name__ == '__main__':
    if len(argv) != 3:
        raise Exception("Wrong number of arguments. Please provide two argumets: script path and word!")

    file_name, word = argv[1], argv[2]
    if not path.isfile(file_name):
        raise Exception("The provided path doesn't point to an existing path!")

    grep(file_name, word)
