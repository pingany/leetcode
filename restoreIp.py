#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,utils
reload(sys)
sys.setdefaultencoding("utf-8")

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        r = []
        self.ria(s, results=r)
        return r

    def ria(self, s, index=0, results=[], ipArray=[None]*4):
        size = 4 - index
        if not s and not size:
            results.append(".".join(ipArray))
            return
        if not s or not size:
            return
        for ipLen in range(1, min(3, len(s))+1):
            substr = s[:ipLen]
            if substr != '0' and substr.startswith('0'):
                continue
            if len(substr) >= 3:
                if int(substr) > 255:
                    continue
            ipArray[index] = substr
            self.ria(s[ipLen:], index+1, results, ipArray)


def doTest(s, lists):
    assert sorted(Solution().restoreIpAddresses(s)) == sorted(lists)

def test():
    doTest("", [])
    doTest("1", [])
    doTest("11", [])
    doTest("111", [])
    doTest("1112", ["1.1.1.2"])
    doTest("1111", ["1.1.1.1"])
    doTest("256256256256", [])
    doTest("256256256255", [])
    doTest("123123123123", ["123.123.123.123"])
    doTest("25525511135", ["255.255.11.135", "255.255.111.35"])
    doTest("010010",["0.10.0.10","0.100.1.0"])

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])