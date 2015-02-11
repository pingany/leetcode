#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,bisect
reload(sys)
sys.setdefaultencoding("utf-8")

def lowerCount(a, lo, hi, x):
    return bisect.bisect_left(a, x, lo, hi)

def upperCount(a, lo, hi, x):
    i = bisect.bisect(a, x, lo, hi)
    return hi - x


def test():
    assert lowerCount([1, 2], 0, 2, 1) == 0
    assert lowerCount([1, 2], 0, 2, 2) == 1
    assert lowerCount([1, 2], 0, 2, 3) == 2
    assert upperCount([1, 2], 0, 2, 2) == 0
    assert upperCount([1, 2], 0, 2, 1) == 1
    assert upperCount([1, 2], 0, 2, 0) == 2

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])