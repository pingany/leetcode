#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        k = m + n - 1
        i = m - 1
        j = n - 1
        while k >= 0:
            if i >= 0 and (j < 0 or (j >= 0 and A[i] > B[j])):
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1
        return A

import random
def ranArray(n):
    return sorted([random.randint(1, 10) for x in range(n)])

def test():
    assert Solution().merge([1, None], 1, [2], 1) == [1, 2]
    assert Solution().merge([3, None], 1, [2], 1) == [2, 3]
    for i in range(10):
        a = ranArray(random.randint(1, 500))
        b = ranArray(random.randint(1, 500))
        c = sorted(a + b)
        a = a + [None]*len(b)
        Solution().merge(a, len(a)-len(b), b, len(b))
        assert c == a

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])