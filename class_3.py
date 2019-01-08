# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:55:10 2019

@author: chenmth
"""

class Calculator: #class名稱第一個字母要大寫
    def __init__(self,name,price,weight=30): #類似Constructor
        self.n = name
        self.p = price
        self.w = weight
        self.add(10,10) #先宣告了 so...
    def add(self,a,b):
        print(a+b) #這邊會先print出
cal = Calculator('kenny',20)
print(cal.n)
print(cal.p)
print(cal.w)
