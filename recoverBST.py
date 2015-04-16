#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)
        pass

def recover(tree):
    if not tree:
        return tree
    misorders = []
    last2Nodes = []
    def pushNode(node):
        if len(last2Nodes) >= 2:
            del last2Nodes[0]
        last2Nodes.append(node)
        if len(last2Nodes) == 2:
            if last2Nodes[0].val > last2Nodes[1].val:
                misorders.append(last2Nodes[:])
        # print last2Nodes, misorders
    def traverse(root):
        if root.left:
            traverse(root.left)
        pushNode(root)
        if root.right:
            traverse(root.right)
        pass
    def swap(nodes, i, j):
        nodes[i].val, nodes[j].val = nodes[j].val, nodes[i].val
        pass
    def ordered(nodes):
        for i in range(1, len(nodes)):
            if nodes[i].val < nodes[i-1].val:
                return False
        return True

    traverse(tree)
    nodes = []

    prev = None
    for a, b in misorders:
        if a != prev:
            nodes.append(a)
        nodes.append(b)
        prev = b

    # print "ndoes", [x.val for x in nodes], 'misorders', misorders, 'last2Nodes', last2Nodes

    n = len(nodes)
    for i in range(n-1):
        for j in range(i+1, n):
            if nodes[j].val < nodes[i].val:
                swap(nodes, i, j)
                if ordered(nodes):
                    return tree
                swap(nodes, i, j)
    return tree

class Solution:
    # @param root, a tree node
    # @return nothing, modify the binary tree in-place instead.
    def recoverTree(self, root):
        recover(root)

def sp(a, b):
    assert treeEquals(recover(a), b)
    pass
def test():
    sp(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(2, TreeNode(1), TreeNode(3)))
    sp(TreeNode(3, TreeNode(1), TreeNode(2)), TreeNode(2, TreeNode(1), TreeNode(3)))
    sp(None, None)

    sp(TreeNode(1), TreeNode(1))

    sp(TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(2, TreeNode(1), TreeNode(3)))

    sp(TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(2, TreeNode(1), TreeNode(3)))
    pass

if __name__ == '__main__':
    test()