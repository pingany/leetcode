#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")

def f(words, start, L):
    l = L
    i = start
    assert len(words[i]) <= l
    l -= len(words[i])
    i += 1
    space = 0
    while l > 0 and i < len(words):
        wlen = len(words[i])
        if l < wlen + 1:
            break
        l -= wlen + 1
        space += 1
        i += 1
    isLastLine = i == len(words)
    line = words[start:i]
    nw = len(line)
    if isLastLine:
        output = " ".join(line)
        output = output + " "*(L - len(output))
        return output, nw
    demitters = max(1, nw - 1)
    space += l
    spaces = [space/demitters for k in range(demitters)]
    leftSpace = space % demitters
    k = 0
    while leftSpace > 0:
        spaces[k] +=1
        k += 1
        leftSpace -= 1
    for k in range(len(spaces)):
        line.insert(k*2+1, " "*spaces[k])
    return "".join(line), nw

class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        k = 0
        lines = []
        while k < len(words):
            line, nw = f(words, k, L)
            lines.append(line)
            k += nw
        return lines

def sp(words, L, lines):
    assert Solution().fullJustify(words, L) == lines

def test():
    sp(['a'], 2, ['a '])
    sp([], 2, [])
    sp(['a'], 1, ['a'])
    sp(['aa', 'aa'], 3, ['aa ', 'aa '])
    sp(['aa', 'aa'], 4, ['aa  ', 'aa  '])
    sp(["This", "is", "an", "example", "of", "text", "justification."], 16, [
   "This    is    an",
   "example  of text",
   "justification.  "
])
    sp(["aa", "aa", "aa", "aa"], 6, ["aa  aa", "aa aa "])
    sp(["What","must","be","shall","be."], 12, ["What must be","shall be.   "])

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])