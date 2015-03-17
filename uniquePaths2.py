#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

def array2(row, col, initValue=None):
    return [[initValue for x in range(col)] for x in range(row)] 

def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    f = array2(rows+1, cols+1, 0)
    for i in xrange(rows-1, -1, -1):
        for j in xrange(cols-1, -1, -1):
            if grid[i][j] == 1:
                # f[i][j] = 0
                pass
            elif i == rows -1 and j == cols - 1:
                f[i][j] = 1
            else:
                f[i][j] = f[i+1][j] + f[i][j+1]
    return f[0][0]
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        return solve(obstacleGrid)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp([[0]], 1)
    sp([[0, 0]], 1)
    sp([[1]], 0)
    sp([[0, 1, 0]], 0)
    sp([
  [0,0,0],
  [0,1,0],
  [0,0,0]
], 2)
    sp([
  [0,0,0],
  [0,1,0],
  [0,0,1]
], 0)
    pass