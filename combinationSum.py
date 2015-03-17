#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

class Solution:
    def __init__(self):
        self.candidates = None
        self.results = None
        self.values = None
        pass
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        if not candidates:
            return [[]] if target == 0 else []
        candidates = sorted(candidates)
        self.candidates = candidates
        self.candidatesNum = len(candidates)
        self.results = []
        self.values = []
        self.selectNext(target, 0)
        return self.results

    def selectNext(self, target, valueIndex):
        value = self.candidates[valueIndex]
        if valueIndex == self.candidatesNum-1:
            if target % value == 0:
                self.results.append(self.values + [value]*(target/value))
            return
        if target < value:
            return
        elif target == value:
            self.results.append(self.values + [target])
            return

        num = target / value
        for i in range(0, num+1):
            left = target-value*i
            if left == 0:
                self.results.append(self.values + [value]*i)
                break
            assert left > 0
            if left < self.candidates[valueIndex+1]:
                # no smaller candidates
                if target % value == 0:
                    self.results.append(self.values + [value]*num)
                break
            self.values += [value]*i
            self.selectNext(left, valueIndex+1)
            del self.values[len(self.values)-i:]
        pass
def solve(candidates, target):
    return Solution().combinationSum(candidates, target)
    pass
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp([], 0, [[]])
    sp([], 1, [])
    sp([1], 1, [[1]])
    sp([1,2], 2, [[2],[1,1]])
    sp([2,3,6,7], 7, [[7],[2,2,3]])
    pass