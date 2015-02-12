#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random,math
from random import randint
from LeetCodeUtils import *

# Return -1, 0 or 1
def compare(x, y):
    i = cmp(x, y)
    if i > 0:
        return 1
    elif i < 0:
        return -1
    else:
        return 0

# Remove tailing 0 in list v, but the final list shouldn't be empty, so [0]/[0,0]
# return [0]
def rstripList(v, x):
    while len(v) > 1:
        if v[-1] == x:
            v.pop()
        else:
            break
    return v

def normalizeVersion(v):
    v = [int(x) for x in v.strip().split('.')]
    return rstripList(v, 0)

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = normalizeVersion(version1)
        v2 = normalizeVersion(version2)
        # print v1, v2
        return compare(v1, v2)

def sp(x, y, r):
    assert Solution().compareVersion(x, y) == r

def test():
    sp("0", "0", 0)
    sp("0", "1", -1)
    sp("1", "1.1", -1)
    sp("1", "1.0", 0)
    sp("1", "1.0.1", -1)
    pass