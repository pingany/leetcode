#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def middleOrderOut(root, results):
    if not root:
        return results
    if root.left:
        middleOrderOut(root.left, results)
    results.append(root.val)
    if root.right:
        middleOrderOut(root.right, results)
    return results

def isSorted(list):
    if not list:
        return True
    i = 1
    l = len(list)
    while i < l:
        if list[i] <= list[i-1]:
            return False
        i += 1
    return True
    pass
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        r = middleOrderOut(root, [])
        return isSorted(r)
        

def test():
    assert isSorted([])
    assert isSorted([1])
    assert isSorted([1, 2])
    assert not isSorted([1, 1])
    assert not isSorted([2, 1])
    assert Solution().isValidBST(None)
    assert Solution().isValidBST(TreeNode(1))
    pass
def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])