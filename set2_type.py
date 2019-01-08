# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:00:34 2019

@author: chenmth
"""

char1 = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6]
char2 = [4,5,6,7,8]
print(set(char1)) #排除重複的, 出來的不會是list
print(type(set(char1))) #是 'set'
print(type(char1)) #是 'list'
print(set(char1).difference(set(char2))) #差集(有1沒有2)(只有set才有交集、差集能用)
print(set(char1).intersection(set(char2))) #交集

String1 = 'Kenny is kenny'
print(list(String1)) #全部都會顯示
print(set(String1)) #重複的不顯示, 但大小寫獨立
print(tuple(String1)) #同list
char3 = {9}
char3.add(10) #tuple, list, str 沒有add的功能
print(char3)

char2.clear() # tuple沒有clear功能
print(char2) #傳回[]
char3.clear()
print(char3) #傳回set()
