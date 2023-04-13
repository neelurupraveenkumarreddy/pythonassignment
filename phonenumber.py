# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 07:21:45 2023

@author: neelu
"""

"""
linear combination of a phone number
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[""]
        for i in digits:
            x=[]
            for j in d[i]:
                for k in res:
                    x+=[k+j]
            res=x
        if digits=="":
            x=[]
            res=x
        return res