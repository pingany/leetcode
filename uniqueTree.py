#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,copy
reload(sys)
sys.setdefaultencoding("utf-8")

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def __init__(self):
        self.nodes = None
        self.results = None
        pass
    # @return a list of tree node
    def generateTrees(self, n):
        self.results = []
        self.nodes = [TreeNode(i) for i in range(1, n+1)]
        self.f(0)
        for node in self.results:
            print "==================="
            self.printNode(node)
            assert self.midfixSortOut(node, []) == range(1, n+1)

    def midfixSortOut(self, node, out):
        if node.left:
            self.midfixSortOut(node.left, out)
        out.append(node.val)
        if node.right:
            self.midfixSortOut(node.right, out)
        return out

    def printNode(self, node, indent=0):
        print ("    "*indent) + (node and str(node.val) or "--")
        if not node:
            return
        self.printNode(node.left, indent+1)
        self.printNode(node.right, indent+1)
        pass

    def findRoot(self, node):
        while node.parent:
            node = node.parent
        return node
        pass


    def bind(self, parent, child, left):
        self.nodes[child].parent = parent
        if left:
            self.nodes[parent].left = child
        else:
            self.nodes[parent].right = child

    def unbind(self, parent, child, left):
        self.nodes[child].parent = None
        if left:
            self.nodes[parent].left = None
        else:
            self.nodes[parent].right = None

    def f(self, index):
        if index == len(self.nodes)-1:
            nodes2 = [copy.copy(node) for node in self.nodes]
            # index to real node
            for node in nodes2:
                if node.left is not None:
                    node.left = nodes2[node.left]
                if node.right is not None:
                    node.right = nodes2[node.right]
                if node.parent is not None:
                    node.parent = nodes2[node.parent]
            self.results.append(self.findRoot(nodes2[0]))
            print "-----------------------"
            return
        self.bind(index, index+1, False)
        self.f(index+1)
        self.unbind(index, index+1, False)

        self.bind(index+1, index, True)
        self.f(index+1)
        self.unbind(index+1, index, True)
        pass

def test2():
    Solution().generateTrees(2)

def test3():
    Solution().generateTrees(3)

def main(args):
    test()
    pass

if __name__ == '__main__':
    main(sys.argv[1:])