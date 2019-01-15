# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 12:05:55 2019

@author: chenmth
"""

import pandas as pd
import numpy as np

A = pd.DataFrame({'A':[0,1,2], 
                 'B':[3,4,5],
                 'C':[0,1,2]},
                 index=['X','Y','Z'])
B = pd.DataFrame({'C':[0,1,2],
                 'M':['A','A','A'], 
                 'D':[3,4,5]},
                 index=['X','Y','F']) 
#right_index和left_index: 保留index項目 可看成針對行的join
C = pd.merge(A, B, left_index=True, right_index=True, how='left') 
print(C)