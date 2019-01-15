# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:36:29 2019

@author: chenmth
"""

import numpy as np

array = np.arange(21,1,-1).reshape((5,4))
print(array)

print(np.mean(array))
print(array.mean())
print(np.average(array)) #三種計算平均方式

array = np.array([[0,6,8,9,11,5,4],[5,3,5,8,9,17,0]])
print(np.median(array)) #找中位數
print(np.cumsum(array)) #數字累加成一個新矩陣
print(np.diff(array)) #數字-前一個數字的值 (矩陣內會少一個數)
print(np.nonzero(array)) #列出非 0 的位置[i][j]
print(np.sort(array)) #每行按順序由小到大排列
print(array.T) #矩陣轉型 A*B -> B*A
print(np.clip(array, 9, 7)) #clip(矩陣, A,B) 所有小於A 的都變成A 大於B 的都變成B