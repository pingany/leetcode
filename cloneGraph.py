
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
class Solution:
    def __init__(self):
        self.newNodes = {}
        pass
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        newNode = self.getNewNode(node)
        for x in node.neighbors:
            if not self.visited(x):
                self.cloneGraph(x)
        newNode.neighbors = [self.getNewNode(x) for x in node.neighbors]
        return newNode

    def visited(self, node):
        return HashWrapper(node) in self.newNodes

    def getNewNode(self, node):
        wrapper = HashWrapper(node)
        if wrapper in self.newNodes:
            return self.newNodes[wrapper]
        self.newNodes[wrapper] = newNode = UndirectedGraphNode(node.label)
        return newNode

def dfs2(node, visited, results):
    w = HashWrapper(node)
    visited.add(w)
    results.append(node)
    for x in node.neighbors:
        if HashWrapper(x) not in visited:
            dfs2(x, visited, results)
    pass

def dfs(node):
    if not node:
        return []
    results = []
    dfs2(node, set(), results)
    return results

def dfsValues(node):
    results = dfs(node)
    return [x.label for x in results]
    pass

def createGraph(nodesCount):
    assert nodesCount >= 0
    if nodesCount == 0:
        return None
    nodes = [UndirectedGraphNode(randint(1, 100)) for x in range(nodesCount)]
    n = nodesCount
    for i in range(0, n-1):
        for j in range(i+1, n):
            if randint(0, 2) != 0:
                nodes[i].neighbors.append(nodes[j])
                nodes[j].neighbors.append(nodes[i])
    return nodes[0]
    pass

def sp(node):
    out1 = dfsValues(node)
    node2 = Solution().cloneGraph(node)
    out2 = dfsValues(node2)
    assert out1 == out2
def test():
    assert None ==Solution().cloneGraph(None)

    node = UndirectedGraphNode(1)
    assert 1 ==Solution().cloneGraph(node).label
    pass

def testR():
    for i in range(0, 20):
        node = createGraph(i)
        sp(node)
    pass
