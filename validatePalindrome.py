#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")

a = ord('a')
z = ord('z')
n0 = ord('0')
n9 = ord('9')

def isAlphaNumberic(x):
    x = ord(x)
    return (x >= a and x <= z) or (x >= n0 and x <= n9)

def normalize(s):
    return "".join([x for x in s.lower() if isAlphaNumberic(x)])
def isPalindrome(s):
    s = normalize(s)
    i = 0
    j = len(s) -1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        return isPalindrome(s)

def test():
    assert isAlphaNumberic('a')
    assert isAlphaNumberic('z')
    assert isAlphaNumberic('0')
    assert isAlphaNumberic('9')
    assert not isAlphaNumberic(' ')
    assert '' == normalize('')
    assert '' == normalize(' ,,.,..#@!#')
    assert Solution().isPalindrome("race a car") == False
    assert Solution().isPalindrome("A man, a plan, a canal: Panama")

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])