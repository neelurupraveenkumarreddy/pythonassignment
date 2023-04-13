# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 07:15:33 2023

@author: neelu
"""
"""
return the poistion of added numbers to give the value of target
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    l+=[i, j]
        return l