# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 11:44:49 2019

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
#indicator: 會說明是哪種合併方式(擺每一行判斷) 默認True
C = pd.merge(A, B, on=['C','M'], how='right', indicator='ABC') #默認inner
print(C)