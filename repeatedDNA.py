#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

x = {'A':0, 'G':1, 'C':2, 'T':3}
def toint(s, start, end):
    r = 0
    i = start
    while i < end:
        r = (r << 2) | x[s[i]]
        i += 1
    return r

def f(s, n):
    map = {} #collections.defaultdict(lambda:0)
    e = len(s)-n
    i = 0
    while i <= e:
        r = toint(s, i, i+n)
        if r not in map:
            map[r] = [1, s[i:i+n]]
        else:
            map[r][0] += 1
        i += 1
    # print "===", map
    return [value[1] for key, value in map.items() if value[0] > 1 ]
class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        return f(s, 10)

def test():
    assert f('', 10) == []
    assert f('A', 10) == []
    assert f('A', 1) == []
    assert f('AA', 1) == ['A']
    assert f('AACC', 1) == ['A', 'C']
    assert f('AACC', 2) == []
    assert f('ACAC', 2) == ['AC']
    assert f('AACAC', 2) == ['AC']
    assert sorted(f('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT', 10)) == ["AAAAACCCCC", "CCCCCAAAAA"]
    pass
def test2():
    print f(json.load(open('repeatedDNA.in')), 10)