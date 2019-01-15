# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 10:46:40 2019

@author: chenmth
"""

import pandas as pd
import numpy as np

#append只能綜向新增, 不可橫向新增, 故沒有axis設定 類似concate

A = pd.DataFrame(np.zeros((5,3)),
                 index=np.arange(5), columns=np.arange(3))
B = pd.DataFrame(np.ones((5,3)),
                 index=np.arange(5), columns=[0,1,'C'])
print(A)
print(B)

print(A.append(B, ignore_index=True)) #把B加到A下方, 若項目沒東西則給Nan, 沒項目則給項目
print(A.append([B,B], ignore_index=True)) #也可多加或重複加

C = pd.Series([2,2,2,2]) #只能列出"行"無法列出"列"
print(C)
print(B.append(C, ignore_index=True))