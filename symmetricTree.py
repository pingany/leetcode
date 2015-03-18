#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *


def treeSymmetric(n1, n2):
    if n1 == n2:
        return True
    if not n1 or not n2:
        return False
    if n1.val == n2.val:
        return treeSymmetric(n1.left, n2.right) and treeSymmetric(n1.right, n2.left)
    return False

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        return treeSymmetric(root.left, root.right)

def solve(root):
    return Solution().isSymmetric(root)

def sp(*a):
    assert treeEquals(*a[:-1]) == a[-1]
    pass
def test():
    sp(None, None, True)
    sp(None, TreeNode(0), False)
    sp(TreeNode(0), TreeNode(0), True)
