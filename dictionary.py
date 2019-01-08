# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 13:07:28 2019

@author: chenmth
"""
#dictionary can be any types even function or array

dic = {"kenny" : "man"} #{a:b} 表示a配對到b
print(dic)
print(dic["kenny"])
dic = {"kenny" : "man", "mary" : "woman"} 
print(dic)
print(dic["mary"])
print("man" in dic) #false, 冒號後不能算是集合內的元素
print("kenny" in dic) #true
del dic["kenny"] #從字典內刪除資料
print(dic)
dic["new one"]="people" #字典內新增, 沒有一定順序
print(dic)
dic["kenny"]="man" #字典內新增, 沒有一定順序
print(dic)
dic["uncle"]="man" #字典內新增, 沒有一定順序
print(dic)

dic = {x:x*2 for x in [1,2,3]} #字典從list內抓出資料轉成x
print(dic)

dic = {"array":[1,2,3], "dictionary":{'a':1, 'b':2}}
print(dic)
print(dic["array"][1]) #2
print(dic["dictionary"]["a"]) #1