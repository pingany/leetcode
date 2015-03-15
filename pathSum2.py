#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
class Solution:
    def __init__(self):
        self.sum = 0
        self.path = []
        self.results = []
        pass
    
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if not root:
            return []
        self.sum = sum
        self.path = []
        self.results = []
        self.f(root)
        return self.results

    def f(self, root):
        if not root.left and not root.right:
            self.path.append(root.val)
            if sum(self.path) == self.sum:
                self.results.append(self.path[:])
            self.path.pop();
            return
        self.path.append(root.val)
        if root.left:
            self.f(root.left)
        if root.right:
            self.f(root.right)
        self.path.pop()
        pass

def solve(root, sum):
    return Solution().pathSum(root, sum)
    pass
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp(None, 0, [])
    sp(None, 1, [])
    sp(TreeNode(1), 1, [[1]])
    sp(TreeNode(1, TreeNode(2)), 3, [[1, 2]])
    sp(TreeNode(1, TreeNode(2)), 1, [])
    sp(TreeNode(1, TreeNode(2), TreeNode(2)), 3, [[1, 2], [1, 2]])
    pass