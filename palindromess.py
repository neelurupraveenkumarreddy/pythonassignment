# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 06:46:11 2023

@author: neelu
"""
"""
printing palindromes position in given list
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
"""
words=[]
k=int(input("Enter number of words you will enter in words list"))
for i in range(k):
    words+=[input()]
s=[]
for i in range(len(words)):
    for j in range(i+1,len(words)):
        k=[]
        r=[]
        m=words[j][::-1]
        print(m)
        if words[i]==m:
            k=[i, j]
            r=[j,i]
            s=s+[k]+[r]
print(s)