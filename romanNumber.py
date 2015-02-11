#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,utils
reload(sys)
sys.setdefaultencoding("utf-8")

table = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
]
class Solution:
    # @return a string
    def intToRoman(self, num):
        s = []
        for t in table:
            if num >= t[0]:
                s.append(t[1]*(num/t[0]))
                num %= t[0]
        return "".join(s)

def sp(num, roman):
    assert Solution().intToRoman(num) == roman

def test():
    sp(1, 'I')
    sp(2, 'II')
    sp(4, 'IV')
    sp(5, 'V')
    sp(42, 'XLII')
    sp(100, 'C')
    sp(1000, 'M')
    sp(500, 'D')
    sp(501, 'DI')
    sp(550, 'DL')
    sp(530, 'DXXX')
    sp(707, 'DCCVII')
    sp(890, 'DCCCXC')
    sp(1500, 'MD')
    sp(1800, 'MDCCC')
    sp(900, 'CM')
    sp(9, 'IX')
    sp(400, 'CD')
    sp(500, 'D')
    sp(600, 'DC')
    sp(700, 'DCC')

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])