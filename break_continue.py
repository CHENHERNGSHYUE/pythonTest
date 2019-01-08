# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 16:48:25 2019

@author: chenmth
"""

#break & continue只能在 for 或 while 迴圈內用

n=0
while n<10:
    if n==5:
        break
    print(n)
    n += 1
print('Final n is', n)

m=0
for x in [0,1,2,3,4,5,6,7,8,9,10]:
    if x%2 == 0: #抓x是偶數
        continue #偶數都跳過 重新開始迴圈
    print(x)
    m += 1
print('Final m is', m)

#找出平方根
a=int(input('輸入數值:'))
for i in range(a):
    if i*i==a:
        print('整數平方根是',i)
        break
    else:
        print('沒有整數平方根') #break後 不會再進入else