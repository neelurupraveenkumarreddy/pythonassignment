# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 07:09:48 2023

@author: neelu
"""
"""
adding 1 to given number in a list form
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""
digits=[]
n=int(input("number of digits you will enter"))
for i in range(n):
    digits+=[int(input())]
s=""
for i in range(len(digits)):
    s=s+str(digits[i])
    k=int(s)+1
k=str(k)
list=[]
for i in k:
    list+=[i]
print(list)