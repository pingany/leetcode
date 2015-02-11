#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,operator
reload(sys)
sys.setdefaultencoding("utf-8")

def div(a,b):
    return int(float(a)/b)

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": div,
}
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t in ops:
                b = stack.pop()
                a = stack.pop()
                # print a, b, ops[t]
                stack.append(ops[t](a, b))
            else:
                stack.append(int(t))
        return int(stack[0]) if stack else 0


def sp(exp, result):
    assert Solution().evalRPN(exp) == result

def test():
    sp(["2", "1", "+", "3", "*"] , 9)
    sp(["4", "13", "5", "/", "+"], 6)
    sp([], 0)
    sp(["1"], 1)
    sp(["0"], 0)

def test2():
    sp(["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22)

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])