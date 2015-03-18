#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(root, sum):
    if not root:
        return False
    # leaf
    if not root.left and not root.right:
        return root.val == sum

    # not leaf
    ret = (root.left and solve(root.left, sum-root.val)) or \
            (root.right and solve(root.right, sum-root.val))
    return bool(ret)

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        return solve(root, sum)
def sp(*a):
    r = solve(*a[:-1])
    assert r == a[-1]
    assert type(r) == type(a[-1])
    pass
def test():
    sp(None, 0, False)
    sp(None, 1, False)

    tree = TreeNode(1)
    sp(tree, 1, True)
    sp(tree, 0, False)
    sp(tree, 2, False)

    tree = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4))
    sp(tree, 6, True)
    sp(tree, 5, True)
    sp(tree, 3, False)

    sp(TreeNode(-2, TreeNode(-3)), -5, True)
    sp(TreeNode(-2, TreeNode(-3)), -6, False)
    sp(TreeNode(-2, TreeNode(-3)), 6, False)
    pass