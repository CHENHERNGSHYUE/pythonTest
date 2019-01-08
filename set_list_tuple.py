# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:22:07 2019

@author: chenmth
"""

set1 = {'a','b','c'}
list1 = [1,2,3]
tuple1 = ('A','B','C')

#移除一次只能一個, 不可多個
set1.remove('a') #若要remove的資料裡面沒有, 則報錯
set1.discard('e') #若要discard的資料裡面沒有, 不會報錯
print(set1)
set1.discard('b')
print(set1)

list1.remove(1) #list沒有discard功能
print(list1)

#tuple沒有remove也沒有discard功能


