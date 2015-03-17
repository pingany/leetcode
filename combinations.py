#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
class Solution:
    def __init__(self):
        self.n = None
        self.k = None
        self.resuls = None
        self.numbers = None
        pass
    # @return a list of lists of integers
    def combine(self, n, k):
        if n < k:
            return []
        self.n = n
        self.k = k
        self.resuls = []
        self.numbers = [None]*k
        self.selectNext(0, 1)
        return self.resuls

    def selectNext(self, position, minValue):
        if position == self.k:
            self.resuls.append(self.numbers[:])
            return
        maxValue = self.n - self.k + position+1
        for value in xrange(minValue, maxValue+1):
            self.numbers[position] = value
            self.selectNext(position+1, value+1)

def solve(n, k):
    return Solution().combine(n, k)
def sp(*a):
    assert solve(*a[:-1]) == sorted(a[-1])
    pass
def test():
    sp(0,0, [[]])
    sp(2,0, [[]])
    sp(0,1, [])
    sp(1,2, [])
    sp(1,1, [[1]])
    sp(2,1, [[1],[2]])
    sp(4, 2, [
          [2,4],
          [3,4],
          [2,3],
          [1,2],
          [1,3],
          [1,4],
        ])
    sp(3, 3, [ [1,2,3]])
    pass