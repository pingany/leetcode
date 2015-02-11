#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,utils,bisect
reload(sys)
sys.setdefaultencoding("utf-8")

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect.bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        numbers = []
        for i in range(len(num)):
            numbers.append((i+1, num[i]))
        numbers.sort(cmp=lambda x, y: x[1]-y[1])
        values = [x[1] for x in numbers]
        i = 0
        for v in values:
            if v <= target/2:
                x = binary_search(values, target-v, i+1)
                if x >= 0 :
                    return tuple(sorted((numbers[i][0], numbers[x][0])))
            i = i + 1

def test():
    assert Solution().twoSum([1, 2], 3) == (1, 2)
    assert Solution().twoSum([2, 1], 3) == (1, 2)
    assert Solution().twoSum([2, 3, 1], 4) == (2, 3)
    assert Solution().twoSum([5, 6], 10) == None

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])