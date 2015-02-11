#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,utils
reload(sys)
sys.setdefaultencoding("utf-8")

def array2(row, col, initValue):
    return [[initValue for x in range(col)] for x in range(row)] 

class Solution:
    def __init__(self):
        self.s1 = None
        self.s2 = None
        self.s3 = None
        self.caches = None
        pass
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.caches = array2(len(s1)+1, len(s2)+1, None)
        return self.f(len(s1), len(s2))

    def f(self, j, k):
        if j == 0 and k == 0:
            return True
        if self.caches[j][k] != None:
            return self.caches[j][k]
        if j > 0:
            if self.s1[j-1] == self.s3[j+k-1]:
                if self.f(j-1, k):
                    self.caches[j][k] = True
                    return True
        if k > 0:
            if self.s2[k-1] == self.s3[j+k-1]:
                if self.f(j, k-1):
                    self.caches[j][k] = True
                    return True
        self.caches[j][k] = False
        return False

def test():
    assert Solution().isInterleave("123", "123", "123123")
    assert Solution().isInterleave("123", "123", "112233")
    assert Solution().isInterleave("123", "123", "121233")
    assert Solution().isInterleave("123", "123", "112323")

    assert not Solution().isInterleave("123", "123", "121234")
    assert not Solution().isInterleave("123", "123", "122133")
    assert not Solution().isInterleave("123", "123", "112332")

    assert Solution().isInterleave("", "", "")
    assert Solution().isInterleave("1", "", "1")
    assert Solution().isInterleave("", "1", "1")
    assert not Solution().isInterleave("", "2", "1")
    assert Solution().isInterleave("2", "1", "12")
    assert Solution().isInterleave("2", "1", "21")
    pass
def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])