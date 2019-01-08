# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:46:16 2019

@author: chenmth
"""

class Calculator: #class名稱第一個字母要大寫
    Name = 'kenny'
    def add_function(self,a,b): #self有點類似static
        return a+b
    def minus_function(self,a,b):
        return a-b
    def times_function(self,a,b):
        return a*b
    def divide_function(self,a,b):
        return a//b
cal=Calculator()
print(cal.Name)
print(cal.add_function(10,10)) #若前面拿掉"self" 就會跳error
print(cal.minus_function(10,10))
print(cal.times_function(10,10))
print(cal.divide_function(10,10))