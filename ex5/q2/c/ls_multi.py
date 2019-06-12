#!/usr/bin/python3

import os
import hashlib
import multiprocessing 
from multiprocessing import Pool
from calc_hex import calc_hex
import sys

directory = sys.argv[1]

all_files = []
i=0
for root,dirs,files in os.walk(directory):
    for filename in files:
        i += 1
        file_path = os.path.join(root,filename)
        readable_hash = hashlib.md5(file_path.encode()).hexdigest();
        #print (i,",",file_path,",",readable_hash)
        all_files.append((i,file_path))


p=Pool(2)
p.map(calc_hex, all_files)




