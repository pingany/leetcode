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
        self.word = None
        self.rows = None
        self.cols = None
        self.visited = None
        pass
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if not word:
            return True
        if not board or not board[0]:
            return False
        self.board = board
        self.word = word
        self.rows = len(board)
        self.cols = len(board[0])
        self.visited = array2(self.rows, self.cols, False)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == word[0]:
                    if self.dfs(i, j, 0):
                        return True
        return False

    def dfs(self, row, col, wordPos):
        if wordPos == len(self.word)-1:
            return True
        self.visited[row][col] = True
        for diff in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            i = row +diff[0]
            j = col + diff[1]
            # print self.__dict__, locals()
            if i >=0 and i < self.rows and \
                    j >=0 and j < self.cols and \
                    (not self.visited[i][j]) and \
                    self.board[i][j] == self.word[wordPos+1] :
                # print "ok i, j", i, j
                if self.dfs(i, j, wordPos+1):
                    return True
        self.visited[row][col] = False
        return False

def solve(board, word):
    return Solution().exist(board, word)
    pass
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test1():
    sp(["ABC"], "ABC", True)
    sp(["A","B","C"], "ABC", True)
    pass
def test():
    sp([], "", True)
    sp(["A"], "", True)
    sp([], "ABC", False)
    sp(["A"], "ABC", False)
    sp(["AC"], "ABC", False)
    sp(["ACB"], "ABC", False)
    sp(["ABC"], "ABC", True)
    sp(["A","B","C"], "ABC", True)

    board = [
          "ABCE",
          "SFCS",
          "ADEE"
        ]
    sp(board, "ABCCED", True)
    sp(board, "SEE", True)
    sp(board, "ABCB", False)
    pass

if __name__ == '__main__':
    test1()