# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:38:34 2019

@author: chenmth
"""

try:
    file=open('try_j.txt','r')
except Exception as e:
    print(e)
    feedback = input("Do you want to creat new file?")
    if feedback == "y":
        file=open('try_kenny.txt','w')
        file.write("test pass")
        file.close()
    else:
        print("You don't creat any files")
