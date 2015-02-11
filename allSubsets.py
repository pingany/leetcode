#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")

class Solution:
    def __init__(self):
        self.subset = []
        self.results = []
        pass
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        s = sorted(S)
        self.subset = [None]*len(s)
        self.f(s, 0, self.subset)
        return self.results
        
    def f(self, s, i, subset):
        if i == len(s):
            self.results.append(filter(lambda x : x is not None, subset))
            return
        subset[i] = None
        self.f(s, i+1, subset)
        subset[i] = s[i]
        self.f(s, i+1, subset)

def sp(x, y):
    assert sorted(Solution().subsets(x)) == sorted(y)

def test():
    sp([], [[]])
    sp([1], [[], [1]])
    sp([0], [[], [0]])
    sp([2, 3, 1], [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
])
def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])