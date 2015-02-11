


#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json
reload(sys)
sys.setdefaultencoding("utf-8")


# def array2(row, col, initValue=None):
#     return [[initValue for x in range(col)] for x in range(row)] 

class SolutionSimple:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        reverseN = range(n-1, -1, -1)
        reverseM = range(m-1, -1, -1)

        f2 = [None]*(n+1)
        f2[n] = True
        for j in reverseN:
            f2[j] = p[j] == '*' and f2[j+1]

        f1 = [None]*(n+1)
        for i in reverseM:
            f1[n] = False
            for j in reverseN:
                x = p[j]
                if x == '*':
                    f1[j] = f1[j+1] or f2[j] or f2[j+1]
                elif x == '?':
                    f1[j] = f2[j+1]
                else:
                    f1[j] = s[i] == p[j] and f2[j+1]
            f2, f1 = f1, f2

        return f2[0]

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        # special handle this, because ''.split('*') == ['']
        if not p:
            if s:
                return False

        mustStartWith = True
        ps = p.split("*")
        i = 0
        arrayIndex = 0
        for subp in ps:
            mustEndWith = False
            if arrayIndex == len(ps) - 1:
                mustEndWith = True
            if subp:
                if mustStartWith:
                    if not self.exactStartWith(s, i, subp):
                        return False
                    if mustEndWith:
                        return i + len(subp) == len(s)
                    i += len(subp)
                else:
                    if mustEndWith:
                        return self.exactEndWith(s, i, subp)
                    j = self.indexOf(s, i, subp)
                    if j < 0:
                        return False
                    i = j + len(subp)
            else:
                if mustEndWith:
                    return True
            arrayIndex += 1
            mustStartWith = False
        return i == len(s)

    def exactStartWith(self, s, i, p):
        if not p:
            return True
        if len(s) - i < len(p):
            return False
        for j in range(0, len(p)):
            if p[j] == '?' or s[i+j] == p[j]:
                continue
            else:
                return False
        return True

    def exactEndWith(self, s, i, p):
        return self.exactStartWith(s, max(i, len(s)-len(p)), p)

    def indexOf(self, s, i, p):
        for j in range(i, len(s)-len(p)+1):
            if self.exactStartWith(s, j, p):
                return j
        return -1

def isMatch(a, b):
    return Solution().isMatch(a, b)

def testBasic():
    assert Solution().exactStartWith("123", 0, "?")
    assert Solution().exactStartWith("123", 0, "1?")
    assert Solution().exactStartWith("123", 0, "1?3")
    assert Solution().exactStartWith("123", 1, "23")
    assert Solution().exactStartWith("123", 2, "3")
    assert not Solution().exactStartWith("123", 3, "3")
    assert not Solution().exactStartWith("123", 4, "3")
    assert not Solution().exactStartWith("123", 0, "3")
    assert not Solution().exactStartWith("123", 1, "3")
    assert  Solution().exactEndWith("123", 1, "3")
    assert  Solution().exactEndWith("123", 1, "2?")

    assert Solution().indexOf("123", 0, "?") == 0
    assert Solution().indexOf("123", 0, "?3") == 1
    assert Solution().indexOf("123", 0, "?2") == 0
    assert Solution().indexOf("123", 0, "?32") == -1

def test():
    assert isMatch('', '') == True
    assert isMatch('', '?') == False
    assert isMatch('', '*') == True
    assert isMatch('', 'a') == False

    assert isMatch('a', 'a') == True
    assert isMatch('a', '?') == True
    assert isMatch('a', '*') == True
    assert isMatch('a', '?*') == True
    assert isMatch('aa', '*') == True
    assert isMatch('aa', '') == False

    assert isMatch("aa","a") == False
    assert isMatch("aa","aa") == True
    assert isMatch("aaa","aa") == False
    assert isMatch("aa", "*") == True
    assert isMatch("aa", "a*") == True
    assert isMatch("ab", "?*") == True
    assert isMatch("aab", "c*a*b") == False
    assert isMatch("aab", "a*a*b")
    assert isMatch("aab", "a**b")
    assert isMatch("aab", "*a*b")
    assert isMatch("aab", "***")
    assert isMatch("aabefg", "a**f*g")
    assert isMatch("aabefg", "a**z*g") == False
    assert isMatch("aabefg", "*a**ef*g*")
    assert isMatch("aabefg", "*a**e?*g*")
    assert isMatch("aabefg", "*?**e?*g*")

def test2():
    s, p = json.load(open("globMatch.in"))
    print >>sys.stderr, len(s), len(p)
    print p in s
    # isMatch(s, p)

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])