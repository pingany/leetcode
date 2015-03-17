#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random,bisect
from random import randint
from LeetCodeUtils import *
   
def solve(matrix, target):
    if not matrix or not matrix[0]:
        return False
    lastValueOfEachRows = [row[-1] for row in matrix]
    row = bisect.bisect_left(lastValueOfEachRows, target)

    rows = len(matrix)
    if row == rows:
        return False
    pos = bisect.bisect_left(matrix[row], target)
    assert pos >=0 and pos < len(matrix[row])
    return matrix[row][pos] == target
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        return solve(matrix, target)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp([[]], 0, False)
    sp([[]], 1, False)
    sp([[1]], 1, True)
    sp([[0]], 0, True)
    sp([[0]], 1, False)

    matrix = [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
    sp(matrix, 3, True)
    sp(matrix, 7, True)
    sp(matrix, 50, True)
    sp(matrix, 1, True)
    sp(matrix, 20, True)
    sp(matrix, 10, True)
    sp(matrix, 23, True)
    sp(matrix, 24, False)

    for i in range(100):
        rows = randint(1, 50)
        cols = randint(1, 50)
        a = sorted([randint(1, 100000) for x in range(rows*cols)])
        ai = iter(a)
        matrix = array2(rows, cols)
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = ai.next()

        values = set(a)
        for x in values:
            sp(matrix, x, True)
        for i in range(10000):
            if i not in values:
                sp(matrix, i, False)

    pass