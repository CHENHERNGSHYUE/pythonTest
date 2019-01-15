# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 20:18:54 2019

@author: chenmth
"""

#list = ['3','4','a','-1','b']
#
#try:
#    total = 0
#    for i in list:
#       # if type int(i) is int:
#            total = total + int(i)
#        else:
#            pass
#    print(total)
#except:
#    ValueError

list = ['3', '4', 'a', '-1', 'b']
total = 0
for i in lst:
    try:
        total += int(i)
    except ValueError:
        pass
print(total)    