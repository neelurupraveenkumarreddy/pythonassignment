# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 07:20:16 2023

@author: neelu
"""

"""
reversing an integer
Input: x = -123
Output: -321
"""
class Solution:
    def reverse(self, f: int) -> int:
        r = 0
        x = 0
        h = False
        if 0>f:
            x = -1*f
            h = True
        else:
            x = f
        while x>0:
            i = x%10
            r = r*10+i
            x//=10
        if -2147483648 <= r <= 2147483647:
            if h:
                return -r
            else:
                return r
        else:
            return 0
