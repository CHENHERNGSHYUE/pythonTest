# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:17:07 2019

@author: chenmth
"""
a = True
while a:
    b = int(input("輸入任意數"))
    if b == 1:
        #a = False #(test1)
        #break #(test2)
        continue #(test3)
    else:
        pass
    print("ongoing")
print("ending")