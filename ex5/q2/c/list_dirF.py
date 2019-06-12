#!/usr/bin/python3

import os
import sys

directory = sys.argv[1] #get directory
afiles=[]

#for root, dirs, files in os.walk(directory,topdown=True):
#	for file in files:
#           	files.append(os.path.join( file))

i=0
'''
# Set the directory you want to start from
for dirName, subdirList, fileList in os.walk(directory):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
'''

for (path, dirs, files) in os.walk(directory):
	afiles.append(dirs)
	for f in files:
		print(f)
		afiles.append(f)

