#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
     
class HashWrapper():
    def __init__(self, object):
        self.object = object
    def __hash__(self):
        return id(self.object)
    def __eq__(self, a):
        return self.object == a.object 
        
MIN_INT = -0x80000000
class Solution:
    def __init__(self):
        self.maxInclusive = {}
        pass
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maxInclusive = {}
        return self.maxPathSum2(root)

    def maxPathSum2(self, root):
        if not root:
            return MIN_INT
        return max(\
                 root.val + max(0, self.maxPathSumInclude(root.left))+ max(0, self.maxPathSumInclude(root.right)),\
                 self.maxPathSum2(root.left), \
                self.maxPathSum2(root.right))
    def maxPathSumInclude(self, root):
        if not root:
            return MIN_INT
        hash = HashWrapper(root)
        if hash in self.maxInclusive:
            # print root
            return self.maxInclusive[hash]
        r = max(root.val, root.val + self.maxPathSumInclude(root.left), \
                        root.val + self.maxPathSumInclude(root.right))
        self.maxInclusive[hash] = r
        return r

def solve(root):
    return Solution().maxPathSum(root)
    pass

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test1():
    sp(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)), 11)
    pass
def test():
    # sp(None, 0)
    sp(TreeNode(-1), -1)
    sp(TreeNode(-3), -3)
    sp(TreeNode(-3, TreeNode(-1)), -1)
    sp(TreeNode(-3, TreeNode(0)), 0)
    sp(TreeNode(-3, TreeNode(-4)), -3)
    sp(TreeNode(1), 1)
    sp(TreeNode(1, TreeNode(2)), 3)
    sp(TreeNode(1, TreeNode(2, TreeNode(3))), 6)
    sp(TreeNode(1, TreeNode(2), TreeNode(3)), 6)
    sp(TreeNode(1, TreeNode(2), TreeNode(-3)), 3)
    sp(TreeNode(1, TreeNode(2), TreeNode(-1, TreeNode(4))), 6)
    sp(TreeNode(1, TreeNode(2), TreeNode(-1, TreeNode(-4))), 3)
    for i in range(100):
        solve(RandomTree(10).createTree())
    pass