# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 14:16:40 2019

@author: chenmth
"""

a = [1,2,3]
b = [4,5,6]
zip(a,b) #束向合併
#print(zip(a,b)) 無法print出要的結果
print(list(zip(a,b))) #用list方式show出
for i in zip(a,b):
    print(i*3) #重複print2次
for i,j in zip(a,b):
    print (i*2, j*3) #i=a and j=b 去做計算
c = [7,8,9]
print(list(zip(a,b,c)))

def function(x,y):
    return x*y
print(function(2,3))
print(list(map(function,(2,6),[5]))) #只會算對應到的
print(list(map(function,[2,6],[5,8]))) #map 是用於iterables內的運算 像是tuple,list,set,dictionary

function2 = lambda x,y : x+y #lambda類似java function功能
print(function2(3,3))