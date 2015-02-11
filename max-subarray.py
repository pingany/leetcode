#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json
reload(sys)
sys.setdefaultencoding("utf-8")

class Solution:
    def __init__(self):
        pass
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0
        a = A
        gg = [None]*len(a)
        gg[0] = a[0]
        for i in range(1, len(a)):
            gg[i] = max(a[i], a[i] + gg[i-1])
        assert all([x is not None for x in gg])
        return max(gg)



def sp(input, out):
    assert out == Solution().maxSubArray(input)

def test():
    sp([], 0)
    sp([1], 1)
    sp([-1], -1)
    sp([1, -1, 3], 3)
    sp([-1, 1, 3], 4)
    sp(json.load(open("max-subarray.py.in")), 0)
def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])