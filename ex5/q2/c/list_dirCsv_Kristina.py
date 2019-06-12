#!/usr/bin/python3
import hashlib
import os
import sys
from multiprocessing import Pool	

if(len(sys.argv) != 2):
	print("wrong amount of arguments")
	exit()

def funcHex(job):
	(i,filename)=job
	print(filename)
	print(i," ",filename, " ",hashlib.md5(filename.encode()).hexdigest())
	
directory = sys.argv[1] #get directory
afiles=[]

i=0
for (path, dirs, files) in os.walk(directory):
	for f in files:
		i+=1
		afiles.append((i,f))

p=Pool(2)
p.map(funcHex,afiles)

