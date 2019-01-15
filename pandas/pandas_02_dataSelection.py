# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:15:47 2019

@author: chenmth
"""

import pandas as pd
import numpy as np

dateShowing = pd.date_range('20190101', periods=5)
dataFrameShowing = pd.DataFrame(np.arange(1,21).reshape((5,4)), 
                                index=dateShowing, columns=['A','B','C','D'])
print(dataFrameShowing)
print(dataFrameShowing['B']) #秀出B列的資訊
print(dataFrameShowing.B) #同上述結果 (但限制為string)

#print(dataFrameShowing['2019-01-01']) 整能抓列資訊, 無法抓行
print(dataFrameShowing[1:3])#抓行資訊的方式 抓第一和第二行
print(dataFrameShowing['20190101':'20190103']) #會抓01~03

#根據標籤進行篩選->loc
print(dataFrameShowing.loc['20190102']) #這一行對應到的列資訊和元素內容
print(dataFrameShowing.loc['20190102',:]) #同上 ":"->全部
print(dataFrameShowing.loc['20190102',['A','C']]) #列出20190102 A列和C列資訊
print(dataFrameShowing.loc[:,['A','C']]) #每一行所有A和C的資訊

#根據座標進行篩選->iloc
print(dataFrameShowing)
print(dataFrameShowing.iloc[4,3]) #(行位置,列位置)
print(dataFrameShowing.iloc[0:2,0:2]) #指定位置區間
print(dataFrameShowing.iloc[[0,2],[0,2]]) #指定位置

#綜合篩選->ix (基本上不太會用了,前兩個已經足夠)
print(dataFrameShowing)
print(dataFrameShowing.ix[[0,2],['A','D']]) 

#條件式篩選
print(dataFrameShowing)
print(dataFrameShowing[dataFrameShowing.A>2]) #只列出A列大於2的數