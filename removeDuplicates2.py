#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        a = A
        if not a:
            return 0
        n = len(a)
        k = 0
        i = 0
        while i < n:
            a[k] = a[i]
            k += 1
            i += 1
            count = 1
            while i < n and a[i] == a[i-1]:
                if count < 2:
                    a[k] = a[i]
                    k += 1
                    count += 1
                i += 1
        return k

def removeDuplicatesSimple(a):
    r = []
    map = collections.defaultdict(lambda:0)
    for x in a:
        map[x] += 1
        if map[x] <= 2:
            r.append(x) 
    return r

def sp(a, results):
    origin = a[:]
    k = Solution().removeDuplicates(a)
    assert results == a[:k]
    assert results == removeDuplicatesSimple(origin)

def test():
    sp([], [])
    sp([1], [1])
    sp([1, 1], [1, 1])
    sp([1, 2], [1, 2])
    sp([1, 1, 2], [1, 1, 2])
    sp([1, 1, 1], [1, 1])
    sp([1, 2, 2], [1, 2, 2])
    pass

def test2():
    for i in range(100):
        a = [randint(1, 50) for x in range(i)]
        a.sort()
        expected = removeDuplicatesSimple(a)
        sp(a, expected)
    pass

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])