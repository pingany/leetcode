#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random,itertools
from random import randint
from LeetCodeUtils import *
   
def fact(n):
    if n == 0:
        return 1
    return fact(n-1)*n

# [fact(x) for x in range(0, 10)]
facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def solve(n, k):
    k -= 1
    numbers = range(1, n+1)
    results = []
    for i in range(n-1, -1, -1):
        pos = k / facts[i]
        k %= facts[i]

        results.append(numbers[pos])
        del numbers[pos]
    return "".join([str(x) for x in results])
class Solution:
    # @return a string
    def getPermutation(self, n, k):
        return solve(n, k)

def solveSimple(n, k):
    r = list(itertools.permutations(range(1, n+1)))[k-1]
    return "".join([str(x) for x in r])
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    # assert solveSimple(*a[:-1]) == a[-1]
    pass
def test():
    # print [fact(x) for x in range(0, 10)]
    sp(1, 1, "1")
    sp(2, 1, "12")
    sp(3, 1, "123")
    sp(3, 2, "132")
    sp(3, 3, "213")
    sp(3, 4, "231")
    sp(3, 5, "312")
    sp(3, 6, "321")

    for i in range(5):
        for n in range(1, 10):
            k = randint(1, facts[n])
            sp(n, k, solveSimple(n, k))
    pass
