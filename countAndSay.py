#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def say(a):
    n = len(a)
    k = 1
    results = []
    for i in range(1, n):
        if a[i] == a[i-1]:
            k+=1
            continue
        results.append(k)
        results.append(a[i-1])
    pass
def test():
    pass