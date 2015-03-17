#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S = sorted(S)
        self.a = S
        self.n = len(S)
        self.results =[]
        self.subset = [None]*self.n
        self.selectNext(0, 0)
        return self.results

    def selectNext(self, position, minValueIndex):
        if minValueIndex == self.n:
            # print self.subset[:position]
            self.results.append(self.subset[:position])
            return
        a = self.a
        # put nothing
        self.results.append(self.subset[:position])

        prev = None
        for i in xrange(minValueIndex, self.n):
            if prev != a[i]:
                self.subset[position] = a[i]
                self.selectNext(position+1, i+1)
            prev = a[i]
        pass

def solveSimpleRecusive(a, i, subset, results):
    if i == len(a):
        results.append(tuple(sorted(subset)))
        return
    solveSimpleRecusive(a, i+1, subset, results);
    subset.append(a[i])
    solveSimpleRecusive(a, i+1, subset, results);
    subset.pop()

def solveSimple(a):
    results = []
    solveSimpleRecusive(a, 0, [], results)
    return sorted([list(x) for x in set(results)])
        
def solve(set):
    return Solution().subsetsWithDup(set)
def sp(set, subsets):
    subsets.sort()
    assert sorted(solve(set)) == subsets
    assert solveSimple(set) == subsets
    pass
def test1():
    sp([1,2], [[], [1], [2], [1, 2]])
    pass
def test():
    sp([], [[]])
    sp([1], [[], [1]])
    sp([1,2], [[], [1], [2], [1, 2]])
    sp([1, 2,2], [
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
])
    for i in range(20):
        a = [randint(0, 5) for x in range(10)]
        sp(a, solveSimple(a))
    pass