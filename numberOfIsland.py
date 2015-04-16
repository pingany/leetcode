#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def array2(row, col, initValue=None):
    return [[initValue for x in range(col)] for x in range(row)] 

def solve(grid):
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    visited = array2(rows, cols, False)

    def dfs(i, j):
        assert not visited[i][j]
        visited[i][j] = True
        for e in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x = i + e[0]
            y = j + e[1]
            if x >= 0 and x < rows and y >=0 and y < cols and not visited[x][y] and grid[x][y] == '1':
                dfs(x, y)
        pass

    count = 0
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        return solve(grid)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp(["11110",
"11010",
"11000",
"00000",], 1)
    sp(["11000",
"11000",
"00100",
"00011",
    ], 3)
    pass