# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 13:29:40 2019

@author: chenmth
"""

a = int(input("請輸入數字: ")) #if test
if a<5: #java條件式要用括號 python則可以省略
    print("smaller")
elif a==5:
    print("get!!")
else: #else後面不能加東西 若要給條件請有elif
    print("bigger")

a2 = int(input("請輸入數字: ")) #while test
sum = 0
n = 0
while n<=a2: #有縮徘表示在回圈內
    sum += n
    n +=1
print(sum)

for i in [1,2,3]: #for test 
    print(i) #1 \n 2 \n 3 會跳行
for i in "kenny": 
    print(i)
for i in range(10): #0~9
    print(i)
    
a3 = int(input("請輸入數字: "))
sum = 0
for i in range(a3): #0~a3-1
    sum += i
print (sum)

for i in range(0,11,2): #range(a,b,c) a到b每次移動c個單位
    print(i)
