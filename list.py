# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 11:58:30 2019

@author: chenmth
"""

a = "kenny" #字串內會自行排列 start from 0
print(a)
print(a[0])
print(a[1])
print(a[2:5]) #[a:b] 包含a但不包含b
print(a[1:]) #給開頭不給結尾 => 從開頭後全部算
print(a[-4:]) #會同上, 最後一碼為-1開始往前"減"
print(a[:4]) #同理,給結尾不給開頭 => 算到數字前一位的字符
print(a.index('n')) #找出第一個出現n的位置 => 2
print('n出現的次數是',a.count('n'),'次')

grades = [10,20,30,40,50] #List:有順序可變動的列表
print(grades)
grades[0] = 11 #修改資料1
print(grades)
grades[1:3] = [] #刪除資料1跟2 
print(grades)
grades = grades+[60,70] #新增資料
print(grades)
grades.append(10) #新增資料2
print(grades)
grades[1:1]=[12,13,14] #中間插入
print(grades)
grades.insert(0,10) #中間插入2 insert(a,b) a表示插入位置(前), b表示插入的數值
print(grades)
grades.remove(10) #移除list內的數值 若有重複 先移除第一個出現的
print(grades)
grades.sort() #從小到大排序
print(grades)
grades.sort(reverse=True) #從大到小排序 'T'大寫很重要
print(grades)

grades2 = [[1,2,3],[4,5,6]] #二維陣列 (同樣可做刪除 新增 修改)
print(grades2)
print(grades2[0])
print(grades2[1][1]) #5
print(5 in grades2) #false
print(5 in grades2[1]) #true


print(len(grades)) #顯示出List的長度