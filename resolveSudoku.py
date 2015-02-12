#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

def array2(row, col, initValue):
    return [[initValue for x in range(col)] for x in range(row)] 

range09 = range(0, 9)
range10 = range(1, 10)

class Solution:
    def __init__(self):
        self.cells = array2(9, 10, None)
        self.rows = array2(9, 10, None)
        self.cols = array2(9, 10, None)
        self.spaces = []
        self.board = []
        pass
    def cell(self, i, j):
        return self.cells[(i/3)*3+j/3]

    def put(self, i, j, x):
        self.board[i][j] = x
        self.rows[i][x] = 1
        self.cols[j][x] = 1
        self.cell(i, j)[x] = 1 
    def remove(self, i, j, x):
        self.board[i][j] = None
        self.rows[i][x] = None
        self.cols[j][x] = None
        self.cell(i, j)[x] = None

    def canPut(self, i, j, x):
        return not self.rows[i][x] and not self.cols[j][x] and not self.cell(i, j)[x]

    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.board = board
        spaces = self.spaces = []
        for i in range09:
            for j in range09:
                if board[i][j] == '.':
                    board[i][j] = None
                    spaces.append((i, j))
                else:
                    x = int(board[i][j])
                    self.put(i, j, x)
        ok = self.tryPut(0)
        assert ok
        assert self.fullTrue(board)
        assert self.fullTrue(self.rows,1)
        assert self.fullTrue(self.cols, 1)
        assert self.fullTrue(self.cells,1)
        for i in range09:
            for j in range09:
                board[i][j] = str(board[i][j])
    def fullTrue(self, a, start=0):
        return all([all(x[start:]) for x in a])
        pass
    def tryPut(self, spaceIndex):
        if spaceIndex == len(self.spaces):
            # succeed
            return True
        i, j = self.spaces[spaceIndex]
        for x in range10:
            if self.canPut(i, j, x):
                self.put(i, j, x)
                if self.tryPut(spaceIndex+1):
                    return True
                self.remove(i, j, x)
        return False

def assert99(input):
    assert len(input) == 9
    assert all([len(x) == 9 for x in input ])

def test():
    input = ["53..7....",
             "6..195...",
             ".98....6.",
             "8...6...3",
             "4..8.3..1",
             "7...2...6",
             ".6....28.",
             "...419..5",
             "....8..79"]
    expect = ["534678912",
              "672195348",
              "198342567",
              "859761423",
              "426853791",
              "713924856",
              "961537284",
              "287419635",
              "345286179"]
    assert99(input)
    assert99(expect)
    board = [list(x) for x in input]
    assert99(board)
    Solution().solveSudoku(board)
    output = ["".join(x) for x in board]
    assert99(output)
    assert output == expect
    pass