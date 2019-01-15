# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:20:17 2019

@author: chenmth
"""

import pandas as pd
import numpy as np

array = np.array([5,7,9,8,1,2,3,4,6,np.nan,11,11,10,12,15,14,16,13,17,18]).reshape((5,4))
print(array)
dataFrameShowing = pd.DataFrame(array,columns=['a','b','c','d'])
dataFrameShowing['e']=np.nan
print(dataFrameShowing)

print(dataFrameShowing.dropna(axis=0,how='any'))
print(dataFrameShowing.dropna(axis=0,how='all'))  
print(dataFrameShowing.dropna(axis=1,how='any'))
print(dataFrameShowing.dropna(axis=1,how='all')) 
#all要全部都是nan才會丟 any是只要出現一個就全部丟

#dataFrameShowing=dataFrameShowing=dataFrameShowing.fillna(123) #把所有nan填上一個值
#print(dataFrameShowing)

print(dataFrameShowing.isnull()) #秀出哪邊有nan會返回true

print(np.any(dataFrameShowing.isnull())==True) #回傳是否有資料遺失(T or F)

