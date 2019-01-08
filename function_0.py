# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 14:11:08 2019

@author: chenmth
"""

def function(): #用def 定義function
    a = 1
    b = 2
    c = a+b
    print(c)
function() #若沒調用則print不出任何東西

def function(a,b):
    c=a-b
    print('c is',c)
function(10,3)

def book(author, page, number=50): #有先預給定義的要放在沒定義元素的後面
    print('Author is', author,'\n'
          'Page is', page,'\n'
          'NO. is', number)
book('Kenny', 50)
book('Mary', 60, 'abc') #定義內容可被修改