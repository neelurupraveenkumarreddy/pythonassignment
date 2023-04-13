# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:45:31 2023

@author: neelu
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
 
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p=height
        k=len(height)
        max=0
        for i in range(k):
            for j in range(i+1,k):
                if p[i]>=p[j]:
                    m=p[j]*(j-i)
                else:
                    m=p[i]*(j-i)
                if m>max:
                    max=m
        return max