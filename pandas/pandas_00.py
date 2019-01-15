# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:20:11 2019

@author: chenmth
"""

import pandas as pd #類似字典(dictionary)
import numpy as np #類似列表

dict1 = pd.Series([0,1,2,3,np.nan,5,6,7], dtype='float32') #np.nan 就是none
print(dict1) #默認為float64 (dtype)

dateShowing = pd.date_range('20190111', periods=5) #2019-01-11
print(dateShowing)

dateShowing = pd.date_range('190111', periods=5) #2011-01-19
print(dateShowing)

dataFrameShowing = pd.DataFrame(np.arange(20).reshape((5,4)))
print(dataFrameShowing) #自動生成矩陣 含列跟行標籤 (默認 0~i)

dataFrameShowing = pd.DataFrame(np.arange(20).reshape((5,4)),
                                index=dateShowing, columns=['a','b','c','d'])
print(dataFrameShowing) #自動生成矩陣並自訂列標籤(columns)及行標籤(index)

dataFrameShowing = pd.DataFrame({'A':1,'B':'A','C':'a'}, index=[0,1,2])
print(dataFrameShowing) #定義行數

dataFrameShowing = pd.DataFrame({'A':1,'B':'A','C':'a', 'D':pd.Series([0,1,2])})
print(dataFrameShowing) #若其中一項字典有訂出行, 則不需另外打上 index條件)
print(dataFrameShowing.dtypes) #print出每一列的屬性形態

print(dataFrameShowing.index) #打出行標籤及型態
print(dataFrameShowing.columns) #打出列標籤及型態
print(dataFrameShowing.values) #打出所有元素
print(dataFrameShowing.describe()) #只會列出數字形式的所有資訊