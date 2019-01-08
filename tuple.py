# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 12:36:53 2019

@author: chenmth
"""

grades = (10,20,30,40,50) #小括號(或無括號)表示tuple,有順序但不可變動的列表
print(grades)
print(grades[0])
grades = grades+(60,70) #tuple可新增
print(grades)
print(len(grades))
print(10 in grades) #判斷是否存在 => true
print(20 not in grades) #判斷是否不存在 => false
#grades[0]=[] tuple不可刪除資料
#print(grades)
#grades[0]=11 tuple不可修改資料
#print(grades)
#grades[1:1]=(11,12,13) #tuple不可插入資料
#print(grades)

grades = ((1,2,3),(4,5,6))
print(grades[1][1])
print(1 in grades) #false
print(1 in grades[0]) #true
