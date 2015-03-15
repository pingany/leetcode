#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
class Solution:
    def __init__(self):
        self.sum = 0
        self.path = 0
        pass
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if not root:
            return 0
        self.sum = 0
        self.path = []
        self.f(root)
        return self.sum

    def getInt(self, path):
        s = 0
        for i in path:
            s = s * 10 + i
        return s
        pass

    def f(self, root):
        if not root.left and not root.right:
            self.path.append(root.val)
            self.sum += self.getInt(self.path)
            self.path.pop()
            return
        self.path.append(root.val)
        if root.left:
            self.f(root.left)
        if root.right:
            self.f(root.right)
        self.path.pop()
        pass

def solve(root):
    return Solution().sumNumbers(root)
    pass
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp(None, 0)
    sp(TreeNode(1), 1)
    sp(TreeNode(1, TreeNode(2)), 12)
    sp(TreeNode(1, TreeNode(2), TreeNode(3)), 25)
    pass