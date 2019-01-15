# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:19:48 2019

@author: chenmth
"""

import numpy as np

array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([[4,5,6],[7,8,9]])

arrayA = np.vstack((array1, array2, array1)) #垂直合併 (可以重複)
arrayB = np.hstack((array1, array2)) #水平合併 (可以重複)
print(arrayA)
print(arrayB)
print(array1.shape, arrayA.shape, arrayB.shape)

arrayList = np.array([[1,2,3]])
print(arrayList.shape) #(1,3)
print(arrayList.T)

arrayList = np.array([1,2,3])
print(arrayList.shape) #(3,)
print(arrayList.T) #少一中括號結果會不一樣, 解決方式如下(讓他變成矩陣)

arrayList = np.array([1,2,3])[np.newaxis,:] #給他一個空維度
print(arrayList.T)