#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,utils
reload(sys)
sys.setdefaultencoding("utf-8")

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        return self.minDepthNotNone(root)

    def minDepthNotNone(self, root):
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        elif root.left:
            return 1 + self.minDepth(root.left)
        elif root.right:
            return 1 + self.minDepth(root.right)
        return 1

def sp(root):
    return Solution().minDepth(root)
    pass

def test():
    root = TreeNode()
    assert sp(None) == 0
    assert sp(root) == 1

    root.left = TreeNode()
    assert sp(root) == 2

    root.right = TreeNode();
    assert sp(root) == 2

    root.left.left = TreeNode()
    assert sp(root) == 2

    root.right.right = TreeNode()
    assert sp(root) == 3

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])