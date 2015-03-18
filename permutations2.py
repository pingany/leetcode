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
    def permuteUnique(self, num):
        self.a = num
        self.results = []
        self.selectNext(0)
        return self.results
        
    def selectNext(self, index):
        a = self.a
        if index == len(a):
            self.results.append(self.a[:])
            return
        self.selectNext(index+1)
        used = set([a[index]])
        for i in range(index+1, len(a)):
            if a[i] in used:
                continue
            used.add(a[i])
            # swap
            a[i], a[index] = a[index], a[i]
            self.selectNext(index+1)
            # swap back
            a[i], a[index] = a[index], a[i]
        pass
def solve(a):
    return Solution().permuteUnique(a)
    pass
def sp(a):
    p1 = solve(a)
    p2 = [list(x) for x in set(itertools.permutations(sorted(a)))]
    print p1
    assert sorted(p1) == sorted(p2)
def test1():
    sp([2,2,3,3])
    sp([1,2,2,3,3])
    pass
def test():
    sp([])
    sp([1])
    sp([1,2])
    sp([1,2,3])
    sp([1,1])
    sp([1,1,2])

    for i in range(20):
        a = [randint(1, 3) for x in range(randint(1,5))]
        a.sort()
        sp(a)
    pass