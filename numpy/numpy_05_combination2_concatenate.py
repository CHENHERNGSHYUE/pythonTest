# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:35:05 2019

@author: chenmth
"""
#concatenate->連鎖合併 和 hstack vstack的差異在於後面可放axis
import numpy as np

array1 = np.array([1,2,3])[np.newaxis,:]
array2 = np.array([4,5,6])[np.newaxis,:]

New = np.concatenate((array1,array2,array1,array2)) #默認axis=0
print(New)

New = np.concatenate((array1,array2,array1,array2), axis=1) #做水平合併
print(New)

New = np.concatenate((array1,array2,array1,array2), axis=0) #做垂直合併
print(New)
