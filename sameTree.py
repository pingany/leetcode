#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def treeEquals(n1, n2):
    if n1 == n2:
        return True
    if not n1 or not n2:
        return False
    if n1.val == n2.val:
        return treeEquals(n1.left, n2.left) and treeEquals(n1.right, n2.right)
    return False


class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        return treeEquals(p, q)

def sp(*a):
    assert treeEquals(*a[:-1]) == a[-1]
    pass
def test():
    sp(None, None, True)
    sp(None, TreeNode(0), False)
    sp(TreeNode(0), TreeNode(0), True)
    pass