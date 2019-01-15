# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:13:45 2019

@author: chenmth
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

A = pd.Series(np.random.randn(100), index=np.arange(100)) #random normal distribution
A = A.cumsum()

plt.plot(A) #秀出圖形

B = pd.DataFrame(np.random.randn(2,3), #生成資料 共有三組
                 columns=list('XYZ')) #每組資料名稱分別為 X,Y,Z
print(B)
B = B.cumsum() #累加
print(B)
B.plot()
plt.show() #會秀出哪一個項目表示哪一種顏色

#scatter 只會有兩個屬性(x,y)

C = B.plot.scatter(x='X', y='Y', color='red', label = 'first')
C.plot
print(B)
plt.show()

C = B.plot.scatter(x='X', y='Y', color='red', label = 'first')
B.plot.scatter(x='X', y='Z', color='DarkBlue', label = 'second', ax=C)
#把C的資料加入
plt.show()


