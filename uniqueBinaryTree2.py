#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def tree(val, left, right):
    root = TreeNode(val)
    root.left = left
    root.right = right
    return root

def generateTrees(n, values=None):
    if values is None:
        values = range(1, n+1)
    if n == 0:
        return [None]
    if n == 1:
        return [TreeNode(values[0])]
    r = []
    for i in range(n):
        lefts = generateTrees(i, values[:i])
        rights = generateTrees(n-1-i, values[i+1:])
        for left in lefts:
            for right in rights:
                r.append(tree(values[i], left, right))
    return r


class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return generateTrees(n)
def sp(n, results):
    assert results == len(generateTrees(n))
    pass
def test():
    sp(0, 1)
    sp(1, 1)
    sp(2, 2)
    sp(3, 5)
    print generateTrees(3)
    pass