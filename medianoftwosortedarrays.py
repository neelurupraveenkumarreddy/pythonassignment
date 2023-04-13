# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 07:28:25 2023

@author: neelu
"""

"""
median of two sorted arrays
 Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #merging
        nums3=nums1+nums2
        k=len(nums3)
        #sorting
        for i in range(k):
            for j in range(i+1,k):
                if nums3[j]<nums3[i]:
                    key=nums3[i]
                    nums3[i]=nums3[j]
                    nums3[j]=key
        if k%2==0:
            a=nums3[k/2]
            b=nums3[(k/2)-1]
            ab=a+b
            return ab/2.00000
        else:
            p=nums3[k//2]/1
            print(p)
            return p