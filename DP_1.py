# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 12:43:42 2019

@author: chenmth
"""
import numpy as np

arr = [1,2,4,1,7,8,3] #找出相加最大總和, 相鄰兩數不可選

def dp_opt(arr):
    opt = np.zeros(len(arr)) #令opt為一個array 裡面都是0 =>[0,0,0...] 長度為arr 
    opt[0] = arr[0]
    opt[1] = max(arr[0],arr[1])
    for i in range(2, len(arr)):
        A = opt[i-1]
        B = opt[i-2]+arr[i]
        opt[i]=max(A,B)
    return opt[len(arr)-1]

a=dp_opt(arr)
print(a)
    