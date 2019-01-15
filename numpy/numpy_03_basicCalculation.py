# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:00:49 2019

@author: chenmth
"""

import numpy as np

array1 = np.array([[1,2],[3,4]])
array2 = np.arange(4).reshape((2,2))

print(array1)
print(array2)

#print(array1+array2) #矩陣相加
#print(array1-array2) #矩陣相減

print(np.dot(array1,array2)) #矩陣相乘 (橫*直)

array3 = np.arange(6).reshape((2,3))
print(array2.dot(array3)) #另一種乘法表示 矩陣A*矩陣B A的橫列要=B的直列