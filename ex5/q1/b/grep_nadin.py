#!/usr/bin/python3



import sys



if(len(sys.argv) != 2):
  #  print ("Must be 2 arguments!!")

	exit(1)



word = sys.argv[1]

path = sys.argv[2]



file = open(path)



for line in file.readlines():

	if(word in line):



		print(line)
