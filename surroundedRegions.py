#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def array2(row, col, initValue=None):
    return [[initValue for x in range(col)] for x in range(row)] 

class Solution:
    def __init__(self):
        self.board = None
        self.rows = None
        self.cols = None
        self.visited = None
        pass
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board or not board[0]:
            return
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.visited = array2(self.rows, self.cols, False)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 'O' \
                    and not self.visited[i][j] \
                    and (i == 0 or i == self.rows-1 or j == 0 or j == self.cols -1):
                    self.fakeBfs(i, j)

        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 'O' and not self.visited[i][j]:
                    self.board[i][j] = 'X'
    def fakeBfs(self,row,col):
        self.visited[row][col] = True
        nodes = [(row, col)]
        while len(nodes):
            row, col = nodes.pop()
            for diff in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                i = row +diff[0]
                j = col + diff[1]
                if i >=0 and i < self.rows and \
                        j >=0 and j < self.cols and \
                        self.board[i][j] != 'X' and \
                        (not self.visited[i][j]):
                    self.visited[i][j] = True
                    nodes.append((i,j))
def solve(board):
    Solution().solve(board)
    pass
def sp(board, expected):
    Solution().solve(board)
    assert expected == board
def c(board):
    return [list(x) for x in board]
    pass
def test():
    sp(c(["XXX","XOX","XXX"]), c(["XXX","XXX","XXX"]))
    sp(c(['XXXX', 'XOOX', 'XXOX', 'XOXX']), c(['XXXX', 'XXXX', 'XXXX', 'XOXX']))
    sp(c(['XXX','XOX','XXO']), c(['XXX','XXX', 'XXO']))
    sp([],[])
    sp([[]],[[]])
    sp([['X']], [['X']])
    sp([['O']], [['O']])
    sp([['X','O']], [['X', 'O']])
    pass

def testBig():
    board = c(json.load(open('surroundedRegions.in')))
    print len(board)
    solve(board)
    pass