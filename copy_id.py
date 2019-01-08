# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 14:46:21 2019

@author: chenmth
"""

import copy

a = [1,2,3]
b = a
print(id(a)) #id表示秀出該物件存放記憶體的位置
print(id(b))
print(id(a)==id(b))
b[0]=111
print(a) #因為空間共用, 所以互相影響

c = copy.copy(a) #copy a 的東西, 但存放記憶體空間位置不同
print(c)
print(id(a)==id(c))
c[0] = 1
print(a) #c是copy a來的 但c的變化不影響a

a[0] = [0,1]
print(a)
d = copy.copy(a) #此copy為表面上copy, 但實際內部內容仍為相同
print(id(d[0])==id(a[0])) #so....is true
d[0][0] = [0,1] #會影響到a 因為copy不夠全面
print(a)

e = copy.deepcopy(a)
print(a)
e[0][0] = 3333333333333
print(a) #a內容不變
print(e) #e內容會變
print(id(d[0])==id(e[0]))
