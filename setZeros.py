#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")


def dupMatrix(matrix):
    return [x[:] for x in matrix]

def setZeroesSimple(matrix):
    matrix2 = dupMatrix(matrix)
    rows = len(matrix)
    for row in range(rows):
        cols = len(matrix[row])
        for col in range(cols):
            if matrix2[row][col] == 0:
                for i in range(rows):
                    matrix[i][col] = 0
                for i in range(cols):
                    matrix[row][i] = 0

def setZerosWrong(matrix):
    rows = len(matrix)
    for row in range(rows):
        cols = len(matrix[row])
        for col in range(cols):
            if matrix[row][col] == 0:
                if row == 0 or matrix[row-1][col] != 0:
                    for i in range(rows):
                        matrix[i][col] = 0
                for i in range(cols):
                    matrix[row][i] = 0
                break

def setZeroesSimple2(matrix):
    if not matrix or not matrix[0]:
        return
    rows = len(matrix)
    cols = len(matrix[0])
    zeroRows = [False]*rows
    zeroCols = [False]*cols
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zeroRows[i] = True
                zeroCols[j] = True
    for row in range(rows):
        if zeroRows[row]:
            for i in range(cols):
                matrix[row][i] = 0
    for col in range(cols):
        if zeroCols[col]:
            for i in range(rows):
                matrix[i][col] = 0
    pass

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        setZeroesSimple2(matrix)

def sp(input, out):
    input2 = dupMatrix(input)
    Solution().setZeroes(input2)
    assert input2 == out


from random import randint
def randomTest():
    originalMatrix = [[randint(0, 2)]*2 for i in range(2)]

    matrix = dupMatrix(originalMatrix)
    matrix2 = dupMatrix(originalMatrix)

    setZeroesSimple(matrix2)
    setZeroesSimple2(matrix)
    assert matrix == matrix2, "original matrix:" + str(originalMatrix) + ""

def test():
    sp([], [])
    sp([[1]], [[1]])
    sp([[1,0]], [[0,0]])
    sp([[1,1],[1,0]], [[1,0],[0,0]])
    sp([[0,1],[1,1]], [[0,0],[0,1]])
    sp([[2, 2], [0, 0]], [[0, 0], [0, 0]])

def test2():
    for i in range(100):
        randomTest()
    pass
def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])