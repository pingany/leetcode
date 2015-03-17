#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random,itertools
from random import randint
from LeetCodeUtils import *

class Solution:
    def __init__(self):
        self.a = None
        self.results = None
        pass
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        self.a = num
        self.results = []
        self.selectNext(0)
        return self.results
        
    def selectNext(self, index):
        a = self.a
        if index == len(a):
            self.results.append(self.a[:])
            return
        for i in range(index, len(a)):
            # swap
            a[i], a[index] = a[index], a[i]
            self.selectNext(index+1)
            # swap back
            a[i], a[index] = a[index], a[i]
        pass
def solve(a):
    return Solution().permute(a)
    pass
def sp(a):
    p1 = solve(a)
    p2 = [list(x) for x in itertools.permutations(a)]
    assert sorted(p1) == p2
def test():
    sp([])
    sp([1])
    sp([1,2])
    sp([1,2,3])
    pass