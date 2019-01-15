# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 15:10:27 2019

@author: chenmth
"""

import pandas as pd
import numpy as np

showing1 = pd.DataFrame(np.ones((2,3))*1) #給乘號就能定義矩陣內的數值要等同任意數
showing2 = pd.DataFrame(np.ones((2,3))*2)
showing3 = pd.DataFrame(np.ones((2,3))*3)

#concat方法
print(pd.concat([showing1,showing2,showing3], axis=0)) #直向並列
print(pd.concat([showing1,showing2,showing3], axis=1, ignore_index=True))
 #橫向並列, ignore_index = True 表示忽略原index數值
 
#join方法 類似SQL inner和outer 
showing1 = pd.DataFrame(np.ones((2,3))*1, index=['A','B'], columns=['A','B','C']) 
showing2 = pd.DataFrame(np.ones((2,3))*2, index=['B','C'], columns=['B','C','D'])
print(showing1)
print(showing2)
print(pd.concat([showing1,showing2], join='inner')) #交集留下的概念(比較index為一致的)
print(pd.concat([showing1,showing2], join='outer')) #會補nan成矩形 "默認模式"

print(pd.concat([showing1,showing2], axis=1, join_axes=[showing2.index])) #差集 空的欄位會補上NaN
print(pd.concat([showing1,showing2], axis=1, join_axes=[showing2.columns])) #方向不同結果會很怪(可跟上面比)
print(pd.concat([showing1,showing2], axis=0, join_axes=[showing2.columns]))