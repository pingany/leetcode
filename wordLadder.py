#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def bfsDepth(g, start, end):
    if start == end:
        return 1
    depth = 1
    nodes = [start]
    n = len(g)
    # print n
    visited = [False]*n
    visited[start] = True
    nextLevel = []
    while len(nodes) > 0:
        depth += 1
        del nextLevel[:]
        for node in nodes:
            for e in g[node]:
                if not visited[e]:
                    if e == end:
                        return depth
                    visited[e] = True
                    nextLevel.append(e)
        # swap
        nodes, nextLevel = nextLevel, nodes
        pass
    return 0
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        if start == end:
            return 1
        map = {}
        i = 0
        for x in dict:
            map[x] = i
            i += 1
        for x in (start, end):
            if x not in map:
                map[x] = i
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

        return bfsDepth(g, map[start], map[end])
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
    return Solution().ladderLength(start, end, dict)
    pass
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp("hit", "cog", (["hot","dot","dog","lot","log"]), 5)
    sp("hit", "hit", ["hot","dot","dog","lot","log"], 1)
    sp("hit", "hitxfd", ["hot","dot","dog","lot","log"], 0)
    sp('ab', 'ac', [], 2)
    sp('ab', 'cd', [], 0)
    sp('ab', 'cd', ["ad"], 3)
    pass
def testBig():
    start, end, dict = json.load(open("wordLadder.in"))
    solve(start, end, dict)
    pass

if __name__ == '__main__':
    testBig()