#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        map = {}
        for n in num:
            if n not in map:
                map[n] = 1
            else:
                map[n] += 1
        return max(map.items(), key=lambda x: x[1])[0]

def test():
    assert Solution().majorityElement([1]) == 1
    assert Solution().majorityElement([1, 1]) == 1
    assert Solution().majorityElement([1, 1, 2]) == 1
    assert Solution().majorityElement([1, 1, 2, 3, 2, 2]) == 2

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])