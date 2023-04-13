# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 07:18:37 2023

@author: neelu
"""

"""
palindrome
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        reverse=""
        for i in x:
          reverse=i+reverse
        if reverse==x:
          return True
        else:
          return False