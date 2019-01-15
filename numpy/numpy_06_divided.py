# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:56:31 2019

@author: chenmth
"""

import numpy as np

array = np.arange(9,29).reshape((5,4))

print(array)

#等量分割
print(np.split(array, 5, axis=0)) #橫向切五刀
print(np.vsplit(array,5)) #同上,另一種表示方法 (垂直間之間分開)
print(np.split(array, 2, axis=1)) #垂直切一刀
print(np.hsplit(array,2)) #同上,另一種表示方法 (水平間之間分開)

#不等量分割
print(np.array_split(array, 3, axis=0)) #橫向切三刀
print(np.array_split(array, 8, axis=0)) #若大於排列數, 會產出"多個"新矩陣
print(np.array_split(array, 3, axis=1)) #縱向切三刀