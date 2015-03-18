#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(s, dict):
    dicts = collections.defaultdict(lambda:set())
    for word in dict:
        if word:
            dicts[len(word)].add(word)
    n = len(s)
    f = [False]*(n+1)
    f[n] = True
    lens = sorted(dicts.keys())
    for i in range(n-1, -1, -1):
        for length in lens:
            if i + length > n:
                break
            if f[i+length] and s[i:i+length] in dicts[length]:
                f[i] = True
                break
    return f[0]
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        return solve(s, dict)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp('', ['1'], True)
    sp('leetcode',['leet'], False)
    sp('leetcode',['leet', 'code'], True)
    sp('leetcode',['leet', 'cod'], False)

    sp('aaaaaaa', ['a'], True)
    sp('aaaaaaa', ['a', 'b'], True)
    sp('aaaaaaa', ['aa'], False)
    pass