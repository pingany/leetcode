#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def f(s, n):
    map = {} #collections.defaultdict(lambda:0)
    e = len(s)-n
    i = 0
    while i <= e:
        subs = s[i:i+n]
        if subs not in map:
            map[subs] = 1
        else:
            map[subs] +=1
        i += 1
    print "===", map
    return [key for key, value in map.items() if value > 1 ]
class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        return f(s, 10)

def test():
    assert f('', 10) == []
    assert f('a', 10) == []
    assert f('a', 1) == []
    assert f('aa', 1) == ['a']
    assert f('aabb', 1) == ['a', 'b']
    assert f('aabb', 2) == []
    assert f('abab', 2) == ['ab']
    assert f('aabab', 2) == ['ab']
    assert f('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT', 10) == ["AAAAACCCCC", "CCCCCAAAAA"]
    pass
def test2():
    print f(json.load(open('repeatedDNA.in')), 10)