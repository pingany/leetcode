#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def swapLines(matrix, line1, line2, n):
    x1,y1,diff1 = line1
    x2,y2,diff2 = line2
    # print "swapLines", line1, line2, n
    for i in range(n):
        matrix[y1][x1], matrix[y2][x2] = matrix[y2][x2],matrix[y1][x1] 
        x1 += diff1[0]
        y1 += diff1[1]

        x2 += diff2[0]
        y2 += diff2[1]
    pass
def roateLines(matrix, lines, n):
    nLines = len(lines)
    for i in range(nLines-1, 0, -1):
        swapLines(matrix, lines[i], lines[(i+1)%nLines], n)
        # print matrix
    pass
def rotate(matrix, left, top, n):
    while n > 0:
        roateLines(matrix, ((left, top, (1,0)), (left+n-1, top, (0,1)),\
                 (left+n-1, top+n-1,(-1,0)), (left, top+n-1, (0,-1))), n-1)
        n -= 2
        left +=1
        top +=1
    pass
def rotateImage(matrix):
    n = len(matrix)
    rotate(matrix, 0, 0, n)
    pass
class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        rotateImage(matrix)

def sp(matrix, expected):
    Solution().rotate(matrix)
    assert matrix == expected
def test():
    sp([], [])
    sp([[1]], [[1]])
    sp([[1111]], [[1111]])
    sp([[1,2],[4,3]], [[4, 1],[3,2]])
    sp([[1,2,3],
        [4,5,6],
        [7,8,9]],
       [[7,4,1],
       [8,5,2],
       [9,6,3]])
    pass