# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 11:31:37 2019

@author: chenmth
"""

import pandas as pd
import numpy as np

A = pd.DataFrame({'A':[0,1,2], # X:[] X表示列欄位名稱
                 'B':[3,4,5],
                 'C':[0,1,2],
                 'M':['A','A','A']})
B = pd.DataFrame({'C':[0,1,2],
                 'M':['A','A','V'], #後面只會有前兩個, 因為A,V對不上
                 'D':[3,4,5], #若重複會以後面的為主 欄位名稱必須"唯一"
                 'E':[4,5,6]}) #key名稱需一致, 不然跳empty
print(A)

C = pd.merge(A, B, on=['C','M'] ) #On->列裡面的內容需一致, 不然跳empt
print(C)

# how
C = pd.merge(A, B, on=['C','M'], how='inner' ) #默認形式, 交集
print(C)
C = pd.merge(A, B, on=['C','M'], how='outer' ) #默認形式, 聯集和補nan
print(C)
C = pd.merge(A, B, on=['C','M'], how='right' ) #留右邊資訊 ,左邊補nan 
print(C)
C = pd.merge(A, B, on=['C','M'], how='left' )  #留左邊資訊 ,右邊補nan
print(C)