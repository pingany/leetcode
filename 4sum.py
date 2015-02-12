#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random,bisect
from random import randint
from LeetCodeUtils import *
   
def f(a,target):
    a.sort()
    # a = sorted(a)
    n = len(a)
    result = []
    for i in xrange(n-3):
        if i > 0 and a[i] == a[i-1]:
            continue
        for j in xrange(i+1, n-2):
            if j > i+1 and a[j] == a[j-1]:
                continue
            h = j+1-1
            while h < n-1-1:
                h += 1
                if h > j+1 and a[h] == a[h-1]:
                    continue
                left = target - a[i] - a[j] - a[h]
                start = h+1
                k = bisect.bisect_left(a, left, start)
                if k != n and a[k] == left:
                    result.append([a[i], a[j], a[h], a[k]])
                elif k == start:
                    break
    return result

class HashableList():
    def __init__(self, list):
        self.list = list
        hash = 0
        for i in list:
            hash = hash * 31 + i
        self.hash = hash
    def __hash__(self):
        return self.hash

    def __eq__(self, a):
        return self.list == a.list

def conflictPair(p1, p2):
    assert p1[1] < p1[2]
    return p1[1] == p2[1] or p1[2] == p2[1] or p1[2] == p2[2]
def fourSum(a, target):
    a.sort()
    n = len(a)
    sums = []
    for i in xrange(n-1):
        # if i > 0 and a[i] == a[i-1]:
        #     continue
        for j in xrange(i+1, n):
            # if j > i+1 and a[j] == a[j-1]:
            #     continue
            sums.append((a[i]+a[j], i, j))
    # assert sorted(sums) == sums
    sums.sort()
    # print sums
    # result = collections.OrderedDict()
    result = set()
    nsum = len(sums)
    sumValues = [x[0] for x in sums]
    for i in xrange(nsum-1):
        s1 = sumValues[i]
        toFind = target - s1
        k = bisect.bisect_left(sumValues, toFind, i+1)
        if k != nsum and sumValues[k] == toFind:
            j = k
            while j < nsum and sumValues[j] == toFind:
                if not conflictPair(sums[i], sums[j]):
                    result.add(HashableList(sorted((a[sums[i][1]], a[sums[i][2]], a[sums[j][1]], a[sums[j][2]]))))
                j+=1
        elif k == i+1:
            break
    r = ([x.list for x in result])
    r.sort()
    return r

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        return fourSum(num,target)
def sp(a, r):
    assert fourSum(a, 0) == sorted(r)
def test():
    sp([], [])
    sp([1], [])
    sp([1, 2], [])
    sp([1, 2, 3], [])
    sp([1, 2, -3, 0], [[-3, 0, 1, 2]])
    sp([-1, 0, 1, 2, -1, -4, 0], [[-1, 0, 0, 1], [-1, -1, 0, 2]])
    sp([-1, -1, -1, 2, 2, 0], [[-1, -1, 0, 2]])

def test1():
    sp([0, 0, 0, 0, 0, 0, 0], [[0, 0, 0, 0]])
    sp([0, 0, 0, 0, 0, 1, -1], [[0, 0, 0, 0], [-1, 0, 0, 1]])

def test3():
    for i in range(50):
        a = [randint(0, 100) for x in range(i)]
        assert f(a, 200) == fourSum(a, 200)
def test2():
    a, target = json.load(open("4sum.in"))
    # print len(a),target
    fourSum(a, target)    
    pass