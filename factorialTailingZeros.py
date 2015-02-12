#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def fact(x):
    return  x == 1 and 1 or x * fact(x-1)

def factTailZeros(n):
    x = 5
    r = 0
    while x <= n:
        r += n/x
        x *= 5
    return r
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        return factTailZeros(n)
        
def factTailZerosSimple(n):
    r = 0
    s = 1
    for i in range(2,n+1):
        s *= i
        while s % 10 == 0:
            s /= 10
            r += 1
    return r

def sp(x, y):
    assert factTailZeros(x) == y
def test():
    sp(1, 0)
    sp(2, 0)
    sp(5, 1)
    sp(10, 2)
    sp(25, 6)
    sp(30, 7)

    for i in range(1, 31):
        factTailZerosSimple(i) == factTailZeros(i)
    pass


if __name__ == '__main__':
    print fact(30)