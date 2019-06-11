#!/usr/bin/python3

import os
import hashlib
import multiprocessing 
from multiprocessing import Pool


#rootdir = "/home/jonathan"
i=0
for root,dirs,files in os.walk("."):
    for filename in files:
       # print (root,filename)
        i += 1
        file_path = os.path.join(root,filename)
               # with open (os.path.join(root,filename), "rb") as f:
            #bytes =f.read()
        readable_hash = hashlib.md5(file_path.encode()).hexdigest();
        print (i,",",file_path,",",readable_hash)
   # for filename in files:
   #     i += 1
   #     if os.path.isfile:
   #         print (i,",",file_path,",",readable_hash)

#rootdir = "/home/jonathan"
#for entry in os.listdir(rootdir):
#    if os.path.isdir(os.path.join(rootdir, entry)):
#        print(entry)

#for dirname, subdirlist, filelist in os.walk(rootdir):
#    print ('Found directory: %s' % dirname)
#    for fname in filelist:
#        print ('\t%s' % fname)

#filename = input ("enter the file name:")
#with open (filename,"rb") as f:
#    bytes =f.read() #read file as bytes
#    readable_hash = hashlib.md5(bytes).hexdigest();
#    print (readable_hash)
#for root, dirs, files in os.walk("/home/jonathan"):

  
#   print (files)
#for files in os.listdir ("/home/jonathan"):

 #   print (files)
#os.listdir ("/home/jonathan")

    
