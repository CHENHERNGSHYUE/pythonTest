# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 12:08:31 2019

@author: chenmth
"""

import pandas as pd
import numpy as np

A = pd.DataFrame({'number' : [0,1,2],'word' : ['a','b','c']})
B = pd.DataFrame({'number' : [3,4,2],'word' : ['X','Y','Z']})
#suffix(字尾) - 當項目名稱重複, 可額外做區分
C = pd.merge(A, B, on='number', suffixes=['_區分A項目','_區分B項目'], how='outer') 
print(C)
