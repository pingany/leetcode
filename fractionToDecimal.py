#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")

def f(a, b, results, map):
    # print a, b, "map", map
    if a == 0:
        return
    if a in map:
        i = map[a]
        results.insert(i, '(')
        results.append(')')
        return
    map[a] = len(results)
    results.append(a*10/b)
    f(a*10%b, b, results, map)

def fractionToDecimal(a, b):
    if a % b == 0:
        return str(a/b)
    minus = a/b < 0
    a = abs(a)
    b = abs(b)
    results = []
    f(a%b, b, results, {})
    return "%s%d.%s" % ((minus and "-" or ""), a/b, "".join([str(x) for x in results]))

class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        return fractionToDecimal(numerator, denominator)

def test():
    assert fractionToDecimal(1, 2) == '0.5'
    assert fractionToDecimal(1, 40) == '0.025'
    assert fractionToDecimal(1, 1) == '1'
    assert fractionToDecimal(-2, 1) == '-2'

def test2():
    assert Solution().fractionToDecimal(-2, 3) == '-0.(6)'
    assert fractionToDecimal(-50, 8) == '-6.25'
    # assert fractionToDecimal(1, 311) == '0.(6)'
    pass
def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])