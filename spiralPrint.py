#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,utils
reload(sys)
sys.setdefaultencoding("utf-8")

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        r = []
        self.so(r, matrix, 0, 0, len(matrix) > 0 and len(matrix[0]) or 0, len(matrix))
        return r

    def so(self, r, m, left, top, right, bottom):
        if left >= right or top >= bottom:
            return

        for col in xrange(left, right):
            r.append(m[top][col])
        for row in xrange(top+1, bottom):
            r.append(m[row][right-1])
        if bottom - top > 1:
            for col in xrange(right-2, left-1, -1):
                r.append(m[bottom-1][col])
        if right - left > 1:
            for row in xrange(bottom-2, top, -1):
                r.append(m[row][left])
        self.so(r, m, left+1, top+1, right-1, bottom-1)

def test1():
    assert Solution().spiralOrder([]) == []
    assert Solution().spiralOrder([[]]) == []
    assert Solution().spiralOrder([[],[]]) == []
    assert Solution().spiralOrder([[1]]) == [1]
    assert Solution().spiralOrder([[1, 2]]) == [1, 2]
    assert Solution().spiralOrder([[1, 2], [3, 4]]) == [1, 2, 4, 3]
    assert Solution().spiralOrder([
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]) == [1,2,3,6,9,8,7,4,5]
    assert Solution().spiralOrder([
         [ 0, 1, 2, 3 ],
         [ 0, 4, 5, 6 ],
         [ 0, 7, 8, 9 ]
        ]) == [0, 1,2,3,6,9,8,7, 0, 0,4,5]

def main(args):
    pass

if __name__ == '__main__':
    main(sys.argv[1:])