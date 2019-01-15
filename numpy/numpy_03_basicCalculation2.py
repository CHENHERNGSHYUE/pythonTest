# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:13:36 2019

@author: chenmth
"""

import numpy as np

array = np.random.random((4,3)) #三行兩列隨機 0~1的數
#array = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(array)
print(np.max(array)) #矩陣中找最大值

print(np.min(array, axis=1)) #axis=1 找每行中的最小值
print(np.min(array, axis=0)) #axis=0 找每列中的最小值

print(np.sum(array, axis=1)) #axis=1 算每行的總和
print(np.sum(array, axis=0)) #axis=0 算每列的總和

print(np.argmax(array)) #找出最大值的index位置
print(np.argmin(array)) #找出最小值的index位置
