#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = [root] if root else []
        if self.stack:
            self.appendLeft(self.stack[-1])

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

    def appendLeft(self, node):
        node = node.left
        while node:
            self.stack.append(node)
            node = node.left

    # @return an integer, the next smallest number
    def next(self):
        s = self.stack
        ret = s.pop()
        p = ret.right
        if p:
            s.append(p)
            self.appendLeft(p)
        return ret.val

def sp(node, iterList):
    assert iterList == itToList(BSTIterator(node))
def test():
    sp(None, [])
    sp(TreeNode(1), [1])
    sp(TreeNode(1, TreeNode(2), TreeNode(3)), [2, 1, 3])
def testR():
    for i in range(100):
        tree = RandomTree().createTree()
        sp(tree, inOrderOut(tree, []))
    pass