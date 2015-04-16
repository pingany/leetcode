#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def array2(row, col, initValue=None):
    return [[initValue for x in range(col)] for x in range(row)] 

def array3(n1, n2, n3, initValue=None):
    return [array2(n2, n3, initValue) for x in range(n1)]

def fill2(f, v):
    for row in f:
        for i in xrange(len(row)):
            row[i] = v

def solve(matrix, cell1=1):
    if not matrix:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    m = 0
    f = array2(rows+1, cols+1, 0)
    for j in xrange(cols):
        fill2(f, 0)
        for i in xrange(rows-1, -1, -1):
            for w in xrange(1, cols-j+1):
                if matrix[i][j+w-1] == cell1:
                    f[i][w] = f[i+1][w] + w
                    m = max(m, f[i][w])
                else:
                    break
    return m
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        return solve(matrix, '1')

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp([], 0)
    sp([[]], 0)
    sp([[1]], 1)
    sp([[1,1]], 2)
    sp([[1],[1]], 2)
    sp([[1],[0]], 1)
    sp([[0],[1]], 1)
    sp([[1,1], [1,0]], 2)
    sp([[0,1], [1,0]], 1)
    sp([[1,1], [1,1]], 4)
    sp([[1, 1, 1],
        [0, 1, 1],
        [1, 1, 0]], 4)
    pass