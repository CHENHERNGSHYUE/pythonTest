# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 12:47:56 2019

@author: chenmth
"""

a1 = {1,2,3,3} #set 集合, 沒有順序的概念.
print(a1)
#print(a[0]) 因為沒順序, 所以error
print(1 in a1) #true
print(4 in a1) #false

a2 = {2,3,3,4}
a3 = a1&a2 #交集 找出相同的且不重複 => {2,3}
print(a3)
a3 = a1|a2 #聯集 找出全部的且不重複 => {1,2,3,4}
print(a3)
a3 = a1-a2 #差集 a-b a所有-a&b的 => {1}
print(a3)
a3 = a1^a2 #反交集 a^b = a|b 扣除 a&b => {1,4}
print(a3)

a = set("kenny") #把字串拆成集合, print出所有元素但重複不再print
print(a)

