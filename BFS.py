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
    return [[node.val for node in level] for level in results]


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        return bfs(root)

def test():
    node = TreeNode(3,
                TreeNode(9),
                TreeNode(20, 
                    TreeNode(15),
                    TreeNode(7)))
    assert bfs(node) == [
  [3],
  [9,20],
  [15,7]
]
    pass