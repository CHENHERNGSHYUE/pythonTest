# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:08:42 2019

@author: chenmth
"""

text = 'kenny'
text2 = '\nkenny2'
text3 = 'abc'
text4 = '\ndef'

file = open('kenny.txt', 'a') #write 用 'w' read 用 'r' append 用'a' =>加上文字
file.write(text4)
file.close()

file = open('kenny.txt', 'r')
#print(file.read()) #一般讀
print(file.readlines()) #輸出成List [line1, line2, line3,...]
print(file.readline())
print(file.readline())
print(file.readline())
