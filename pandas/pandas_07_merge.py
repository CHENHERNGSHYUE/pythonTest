# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 11:15:51 2019

@author: chenmth
"""

import pandas as pd
import numpy as np

#merge

A = pd.DataFrame({'A':[0,1,2], # X:[] X表示列欄位名稱
                 'B':[3,4,5],
                 'C':[4,5,6],
                 'M':['A','A','A']})
B = pd.DataFrame({'C':[0,1,2],
                 'C':[3,4,5], #若重複會以後面的為主 欄位名稱必須"唯一"
                 'E':[4,5,6],
                 'M':['A','A','A']})
print(A)

C = pd.merge(A,B, on='M') #(A,B, on=C) 合併A跟B矩陣用C區成左右兩列 且C欄位必須同時存在於A矩陣和B矩陣
print(C) #以M區分,故M只會在C矩陣出現一次, C欄位雖重複, 但會被區分成不同名稱