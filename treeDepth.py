#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

def treeDepth(root):
    if not root:
        return 0
    return 1 + max(treeDepth(root.left), treeDepth(root.right))

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        return treeDepth(root)
def sp(*a):
    assert treeDepth(*a[:-1]) == a[-1]
    pass
def test():
    sp(None, 0)
    sp(TreeNode(0), 1)
    sp(TreeNode(0, TreeNode(1)), 2)
    pass