#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def array2(row, col, initValue):
    return [[initValue for x in range(col)] for x in range(row)] 

def f(g):
    if not g or not g[0]:
        return 0
    rows = len(g)
    cols = len(g[0])
    ff = array2(rows, cols, None)
    for row in range(rows-1, -1, -1):
        for col in range(cols-1, -1, -1):
            if row == rows-1 and col == cols-1:
                ff[row][col] = g[row][col]
                continue
            cell = g[row][col]
            x = (1 << 31)
            if row < rows-1:
                x = min(x, cell + ff[row+1][col])
            if col < cols-1:
                x = min(x, cell + ff[row][col+1])
            ff[row][col] = x
    return ff[0][0]

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        return f(grid)
def test():
    assert f([]) == 0
    assert f([[]]) == 0
    assert f([[1]]) == 1
    assert f([[1],[2]]) == 3
    assert f([[1, 2], [3, 4]]) == 7
    assert f([[1, 2, 3, 4]]) == 10
    pass