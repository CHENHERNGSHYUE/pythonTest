# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:07:33 2019

@author: chenmth
"""

import numpy as np

array = np.arange(5,25).reshape((4,5))
print(array)

print(array[1][1]) #11
print(array[1,1]) #11 另一種表示法
print(array[1]) #[10 11 12 13 14]
print(array[1,:]) #冒號表示print出所有數
print(array[:,1]) #冒號表示print出所有數
print(array[1:3,3]) #找出第三列 第一行到第3行的數(不包含第三行)

for i in array:
    print(i) #印出每一行

for i in array.T:
    print(i) #印出每一列
    
print(array.flatten()) #把矩陣轉成list
for i in array.flat:
    print(i) #print出矩陣內所有數值
