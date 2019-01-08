# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 17:18:27 2019

@author: chenmth
"""

def multi(a1,a2):
    print(a1*a2)
value = multi(3,4) #當有呼叫到multi方法, 內部功能就會執行
print(value) #函式內若沒return就不會迴傳值給value, 而是none

def multi(a1,a2):
    #print(a1*a2)
    return a1*a2 #return才有回傳功能
value = multi(3,4)
print('修改後結果是:',value) #函式內若沒return就不會迴傳值給value, 而是none

 