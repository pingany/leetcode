#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def bfs(node):
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
    results = [[node.val for node in level] for level in results]
    results.reverse()
    return results

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        return bfs(root)

def test():
    node = TreeNode(3,
                TreeNode(9),
                TreeNode(20, 
                    TreeNode(15),
                    TreeNode(7)))
    assert bfs(node) == [
  [15,7],
  [9,20],
  [3],
]
    pass