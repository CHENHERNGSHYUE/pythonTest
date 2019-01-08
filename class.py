# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:33:44 2019

@author: chenmth
"""

class Calculator: #class名稱第一個字母要大寫
    Name = 'kenny'
    def add_function(a,b): 
        return a+b
    def minus_function(a,b):
        return a-b
    def times_function(a,b):
        return a*b
    def divide_function(a,b):
        return a//b
add = Calculator.add_function(10,10)
minus = Calculator.minus_function(10,10)
times = Calculator.times_function(10,10)
divide = Calculator.divide_function(10,10)
print(add)
print(minus)
print(times)
print(divide)