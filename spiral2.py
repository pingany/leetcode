#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,utils
reload(sys)
sys.setdefaultencoding("utf-8")

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def generateMatrix(self, n):
        matrix = [None]*n
        for i in range(n):
            matrix[i] = [None]*n
        self.so(1, matrix, 0, 0, n, n)
        return matrix

    def so(self, r, m, left, top, right, bottom):
        if left >= right or top >= bottom:
            return

        for col in xrange(left, right):
            (m[top][col]) = r
            r = r + 1
        for row in xrange(top+1, bottom):
            (m[row][right-1]) = r
            r = r + 1
        if bottom - top > 1:
            for col in xrange(right-2, left-1, -1):
                (m[bottom-1][col]) = r
                r = r + 1
        if right - left > 1:
            for row in xrange(bottom-2, top, -1):
                (m[row][left]) = r
                r = r + 1
        self.so(r, m, left+1, top+1, right-1, bottom-1)

def test1():
    assert Solution().generateMatrix(0) == []
    assert Solution().generateMatrix(1) == [[1]]
    assert Solution().generateMatrix(2) == [[1, 2], [4, 3]]
    assert Solution().generateMatrix(3) == [
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


def main(args):
    pass

if __name__ == '__main__':
    main(sys.argv[1:])