#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def reverseTraverse(g, start, depth, nodeDepth, path, results):
    path.append(start)
    if depth == 1:
        results.append(list(reversed(path)))
        path.pop()
        return
    for e in g[start]:
        if nodeDepth[e] == depth - 1:
            reverseTraverse(g, e, depth-1, nodeDepth, path, results)
    path.pop()
    pass

def bfsDepth(g, start, end):
    if start == end:
        return [[start]]
    depth = 1
    nodes = [start]
    n = len(g)
    # print n
    nodeDepth = [None]*n
    nodeDepth[start] = 1
    visited = [False]*n
    visited[start] = True
    nextLevelNodes = []
    targetDepth = -1
    while len(nodes) > 0:
        if targetDepth > 0:
            break
        depth += 1
        del nextLevelNodes[:]
        for node in nodes:
            if targetDepth > 0:
                break
            for e in g[node]:
                if not visited[e]:
                    if e == end:
                        nodeDepth[e] = depth
                        targetDepth = depth
                        break
                    visited[e] = True
                    nodeDepth[e] = depth
                    nextLevelNodes.append(e)
        # swap
        nodes, nextLevelNodes = nextLevelNodes, nodes
        pass
    if targetDepth < 0:
        return []
    results = []
    # print targetDepth, nodeDepth
    reverseTraverse(g, end, targetDepth, nodeDepth, [], results)
    return results

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        if start == end:
            return [[start]]
        map = {}
        reversedMap = [None]*(len(dict) + 2)
        i = 0
        for x in dict:
            map[x] = i
            reversedMap[i] = x
            i += 1
        for x in (start, end):
            if x not in map:
                map[x] = i
                reversedMap[i] = x
                i += 1
        n = len(map)
        g = [set() for x in xrange(n)]
        for key,index in map.items():
            key = list(key)
            for i in range(len(key)):
                originalKeyI = key[i]
                for j in "abcdefghijklmnopqrstuvwxyz":
                    if j != originalKeyI:
                        key[i] = j
                        s = "".join(key)
                        if s in map:
                            g[index].add(map[s])
                        key[i] = originalKeyI
        # print reversedMap
        # print g
        results = bfsDepth(g, map[start], map[end])
        results = [ [reversedMap[i] for i in path] for path in results]
        return results

    @staticmethod
    def match(s1, s2):
        if len(s1) != len(s2):
            return False
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if diff >= 1:
                    return False
                diff += 1
        return diff == 1
        pass

def solve(start, end, dict):
    return Solution().findLadders(start, end, dict)
    pass
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test1():
    sp("lost", "cost", ["most","fist","lost","cost","fish"], [["lost","cost"]])
    pass
def test():
    sp("hit", "hit", ["hot","dot","dog","lot","log"], [["hit"]])
    sp("hit", "hitxfd", ["hot","dot","dog","lot","log"], [])
    sp('ab', 'ac', [], [['ab', 'ac']])
    sp('ab', 'cd', [], [])
    sp('ab', 'cd', ["ad"], [['ab', 'ad', 'cd']])
    sp("hit", "cog", (["hot","dot","dog","lot","log"]),   [
        ["hit","hot","dot","dog","cog"],
        ["hit","hot","lot","log","cog"]
      ])
    pass
def testBig():
    start, end, dict = json.load(open("wordLadder.in"))
    solve(start, end, dict)
    pass

if __name__ == '__main__':
    testBig()