# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 13:26:04 2019

@author: chenmth
"""

arr = [3,34,4,12,5,2] 
S = 90  #若arr內任意數字和可以等於"S"則return true, else return false
def check(arr,i,s):
        if s==0:
            return True
        elif i==0:
            return arr[0]==s
        elif arr[i]>s:
            return check(arr, i-1, s)
        else:
            A=check(arr, i-1, s-arr[i])
            B=check(arr, i-1, s)
            return A or B
a = check(arr, len(arr)-1, S)
print(a)