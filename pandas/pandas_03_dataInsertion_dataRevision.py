# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:00:23 2019

@author: chenmth
"""

import pandas as pd
import numpy as np

dateShowing = pd.date_range('20190101', periods=5)
dataFrameShowing = pd.DataFrame(np.arange(1,21).reshape((5,4)), 
                                index=dateShowing, columns=['A','B','C','D'])
print(dataFrameShowing)

#改變數值
dataFrameShowing.iloc[1,1]=50
print(dataFrameShowing)
dataFrameShowing.loc['20190103','C']=100
print(dataFrameShowing)
#dataFrameShowing.ix[3:5,'D']=200 ix幾乎不用了
#print(dataFrameShowing)

dataFrameShowing[dataFrameShowing.A>7]=777
print(dataFrameShowing)
dataFrameShowing.C[dataFrameShowing.A>700]=700 #只動C列但條件從A列來
print(dataFrameShowing)

#插入新列
dataFrameShowing['X']=np.NaN
print(dataFrameShowing)

dataFrameShowing['Y']=[99,100,101,102,'zzz'] #元素多一個少一個都不行
print(dataFrameShowing)