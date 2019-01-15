# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:34:55 2019

@author: chenmth
"""

import numpy as np

array = np.array([1,2,3], dtype=np.int8) 
print(array.dtype) #dtype表示array的type 數字表示位元, 越小越省記憶體空間

#創建array
array = np.ones((5,6)) #生成一個五行六列全部為1的矩陣,只有 zero or 1 記得加's'
print(array)

array = np.arange(1,19,5) #[1 6 11 16] arange(x,y,z) 從 x 到 y前一個數 每次跳 z 單位
print(array)

array = np.arange(5) #[0 1 2 3 4]
print(array)

array = array.reshape((2,2)) #reshape(x,y) 把矩陣轉成 2*2 形式
print(array)

array = np.linspace(1,10,4).reshape((2,2)) #linspace(x,y,z) 列出 x到y 中間分成 z等分
print(array)