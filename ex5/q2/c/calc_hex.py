#!/usr/bin/python3

import hashlib

def calc_hex(job):
    (i,file) = job
    print(i,"," , file,",",hashlib.md5(file.encode()).hexdigest())

