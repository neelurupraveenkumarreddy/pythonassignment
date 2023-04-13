# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 07:27:10 2023

@author: neelu
"""

"""
basic caluculator
Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        num=0
        sign=1
        stack=[]
        for ss in s:
            if ss.isdigit():
                num = 10*num + int(ss)
            elif ss in ["-", "+"]:
                res += sign*num
                num = 0
                sign = [-1, 1][ss=="+"]
            elif ss == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif ss == ")":
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign
                