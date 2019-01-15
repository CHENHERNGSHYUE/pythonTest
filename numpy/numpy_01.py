# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:20:54 2019

@author: chenmth
"""

import numpy as np

array = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print(array) #秀出矩陣形式 array不能有逗號且必須是矩形
print(array.ndim) #2 多少維度
print(array.size) #12 (4*3) 多少個元素
print(array.shape) #(4,3) (x,y)->(矩陣數、行、row, 矩陣內部元素、列、column)