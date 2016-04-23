#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import time

try:
    myrange = xrange
except:
    myrange = range

# just storing something once in each cell
def naive(n):
    beg = time.time()
    costs = [ [0 for i in range(n)] for j in range(n) ]
    mid = time.time()
    for i in myrange(n):
        for j in myrange(n):
            costs[i][j] = i+j
    end = time.time()
    print("alloc = {}s - run = {}s".format(mid-beg, end-mid))

# do same thing but essentially do a write and a read
def naive2(n):
    beg = time.time()
    costs = [ [0 for i in range(n)] for j in range(n) ]
    mid = time.time()
    for i in myrange(n):
        for j in myrange(n):
            if j > 0:
                costs[i][j] = costs[i][j-1] + i
    end = time.time()
    print("alloc = {}s - run = {}s".format(mid-beg, end-mid))

# one write and 2 reads
def naive3(n):
    beg = time.time()
    costs = [ [0 for i in range(n)] for j in range(n) ]
    mid = time.time()
    for i in myrange(n):
        for j in myrange(n):
            if j > 0:
                costs[i][j] = costs[i][j-1] + costs[i][j-1] + i
    end = time.time()
    print("alloc = {}s - run = {}s".format(mid-beg, end-mid))
                
import numpy as np

# same as naive using np.array
def npnaive(n):
    beg = time.time()
    costs = np.zeros( (n, n))
    mid = time.time()
    for i in myrange(n):
        for j in myrange(n):
            costs[i, j] = i+j
    end = time.time()
    print("alloc = {}s - run = {}s".format(mid-beg, end-mid))
    
def npnaive2(n):
    beg = time.time()
    costs = np.zeros( (n, n))
    mid = time.time()
    for i in myrange(n):
        for j in myrange(n):
            if j > 0:
                costs[i, j] = costs[i, j-1] + i
    end = time.time()
    print("alloc = {}s - run = {}s".format(mid-beg, end-mid))
    
def npnaive3(n):
    beg = time.time()
    costs = np.zeros( (n, n))
    mid = time.time()
    for i in myrange(n):
        for j in myrange(n):
            if j > 0:
                costs[i, j] = costs[i, j-1] - costs[i, j-1] + i
    end = time.time()
    print("alloc = {}s - run = {}s".format(mid-beg, end-mid))
    



    # ditto but with a dict on tuples
# this is unexpectedly slooow - like 4 times slower
def dict_tuple(n):
    beg = time.time()
    costs = {}
    for i in myrange(n):
        for j in myrange(n):
            costs[i, j] = i+j


import sys
def main():
    args = sys.argv[1:]
    if not (1 <= len(args) <= 2):
        print("wrong nb of args")
        exit(1)
    command = args[0]
    if len(args) == 1:
        dimension = 2000
    else:
        dimension = int(args[1])
    namespace = globals()
    try:
        function = namespace[command]
        function(dimension)
    except Exception as e:
        import traceback
        traceback.print_exc()
    print("Done")

main()
            
