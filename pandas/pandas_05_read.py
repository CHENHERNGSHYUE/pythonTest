# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:51:43 2019

@author: chenmth
"""

import pandas as pd

dataShowing = pd.read_csv('python_test.csv')
print(dataShowing) #index(row) 仍會顯示

#dataShowing.to_pickle('python_test.pickle')
#dataShowing.to_html('python_test.txt')