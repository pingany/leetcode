#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,utils
reload(sys)
sys.setdefaultencoding("utf-8")

class MultiMap(object):
    def __init__(self):
        self.map = {}
    def add(self, key, value):
        if key not in self.map:
            self.map[key] = []
        self.map[key].append(value)

def sortStr(s):
    return "".join(sorted(s))
        
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        maps = MultiMap()
        res = []
        for s in strs:
            maps.add(sortStr(s), s)
        for (key, values) in maps.map.items():
            if len(values) > 1:
                res += values
        return res


def test():
    assert sortStr("ba") == 'ab'
    assert sortStr("ab") == 'ab'
    assert Solution().anagrams(["ab", "ba"]) == ["ab", "ba"]
    assert Solution().anagrams(["ab", "baa"]) == []
    assert Solution().anagrams(["", "baa"]) == []

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])