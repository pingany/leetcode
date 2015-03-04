#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def f(node):
    if not node:
        return (True, 0)
    balanced1, depth1 = f(node.left)
    balanced2, depth2 = f(node.right)
    return (balanced1 and balanced2 and abs(depth1 - depth2) <= 1, 1 + max(depth1, depth2))
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return f(root)[0]

def sp(node, balanced):
    assert f(node)[0] == balanced
    pass
def test():
    sp(None, True)
    sp(TreeNode(0), True)
    sp(TreeNode(0, TreeNode(1)), True)
    sp(TreeNode(0, TreeNode(1), TreeNode(2)), True)
    sp(TreeNode(0, TreeNode(1, TreeNode(3)), TreeNode(2)), True)
    sp(TreeNode(0, TreeNode(1, TreeNode(3))), False)
    pass