# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 14:38:07 2019

@author: chenmth
"""

a = None #Global variable
def function():
    global a 
    a = 20 # from local variable to global variable
    b = 30 # local variable can't be used out of loop
    c = a+b
    print('Sum is',c)
    return c
print('Origin is', a)
function() #執行程式內要求
print(function()) #print 出程式及return的內容
print('New is',a) #要執行function後才能有function內的a值

a=20 # global variable
def fun2():
    global bc #加上這行才能讓最後一句執行
    bc = 10
    return bc
print(a)
print(fun2())
print(bc) #bc 不是global變數故會跳error
