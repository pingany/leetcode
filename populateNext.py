#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def solve(node):
    if not node or not node.left:
        return
    node.left.next = node.right
    node.right.next = node.next.left if node.next else None
    solve(node.left)
    solve(node.right)
    pass

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        return solve(root)


def bfsGroupByLevel(node):
    results = []
    if not node:
        return results
    nodes = [node]
    while nodes:
        results.append(nodes)
        nextLevel = []
        for node in nodes:
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        nodes = nextLevel
    return results

def bfs(node):
    return sum(bfsGroupByLevel(node), [])

def perfectTree(depth):
    if not depth:
        return None
    root = TreeLinkNode(0)
    root.left = perfectTree(depth-1)
    root.right = perfectTree(depth-1)
    return root

def doTest(depth):
    root = perfectTree(depth)
    nodes = bfs(root)
    i = 0
    for node in nodes:
        node.val = i
        i += 1
    solve(root)
    levels = bfsGroupByLevel(root)
    for nodes in levels:
        assert nodes[-1].next == None
        for i in range(len(nodes)-1):
            assert nodes[i].next == nodes[i+1]
    pass

def sp(*a):
    solve(*a[:-1])
    pass
def test():
    sp(None, None)

    node = TreeLinkNode(1)
    sp(node, node)

    node = TreeLinkNode(1)
    node.left = TreeLinkNode(2)
    node.right = TreeLinkNode(3)
    solve(node)
    assert node.left.next == node.right

def testR():
    for depth in range(1,10):
        doTest(depth)
    pass