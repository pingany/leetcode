#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

lastNode = None

def f2(root):
    global lastNode
    # print "lastNode", lastNode, "root", root
    if lastNode:
        lastNode.right = root
    lastNode = root
    left = root.left
    right = root.right
    root.left = None
    root.right = None

    if left:
        f2(left)
    if right:
        f2(right)
    pass

def f(root):
    global lastNode
    if not root:
        return
    lastNode = None
    f2(root)
    pass

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        f(root)

    
def checkResultTree(root):
    while root:
        assert root.left == None
        root = root.right
        pass

def sp(root):
    # print "before: ", root
    preout = preOrderOut(root, [])
    f(root)
    # print "after: ", root
    checkResultTree(root)
    preout2 = preOrderOut(root, [])
    assert preout == preout2
    pass

def test2():

    sp(TreeNode(1, TreeNode(2)))
    sp(TreeNode(1, None, TreeNode(2)))
    pass
def test():
    f(None)

    node = tree = TreeNode(1)
    sp(node)
    assert node == tree and tree.left is None and tree.right is None

    for i in range(1, 100):
        tree = RandomTree().createTree()
        sp(tree)
    pass