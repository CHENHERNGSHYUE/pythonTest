# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:33:18 2019

@author: chenmth
"""

import pickle #類似存取及加工的功能

dic = {'A':'apple', 'B':'bed', 'C':'cat'}

file = open('pickleTest.txt', 'wb') #write in binary, 不能只用w
pickle.dump(dic, file) #dump是倒,拋棄的意思 把dic資料灌入file
file.close()

file2 = open('pickleTest.txt', 'rb') #因為是二進位寫入,故只能用二進位讀取
dic2 = pickle.load(file2)
file2.close()
print(dic2)

with open('pickleTest.txt','rb') as file3: #使用with就不用管是否有記得close
    dic3 = pickle.load(file3) #用完就自動close()了
print(dic3) #同上一段結果
