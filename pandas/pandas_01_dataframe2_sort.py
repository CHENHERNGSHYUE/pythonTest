# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:03:40 2019

@author: chenmth
"""

import pandas as pd
import numpy as np

dataFrameShowing = pd.DataFrame({'A':np.arange(3), 'B':pd.Series([4,5,6]), 
                                 'E':['x','y','z']})

print(dataFrameShowing)

print(dataFrameShowing.sort_index(axis=0, ascending=False)) #對行名稱排序(名稱需同型態)
#ascending=False ->降冪 反之則升冪

print(dataFrameShowing.sort_index(axis=1, ascending=False)) #對列名稱排序(名稱需同型態)

print(dataFrameShowing.sort_values(by='E', ascending=False)) #對某一欄位元素做排序