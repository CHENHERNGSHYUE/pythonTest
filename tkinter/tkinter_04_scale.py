# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:45:58 2019

@author: chenmth
"""

import tkinter as tk

window = tk.Tk()
window.title('Scale Test')
window.geometry('500x500') 

object1 = tk.Label(window, text='Start', bg='yellow', font=('Times New Roman',12),
                   width=10, height=5) #width和height限制為int形式
object1.pack()

def showingNumber(x): #String x
    object1.config(text=x)
    object1.config(width=int(x))
    
scaleShow = tk.Scale(window, label='任意滑動', length=185, orient=tk.HORIZONTAL,
                     tickinterval=5, from_=10, to=20, showvalue=1,
                     command=showingNumber).pack() 
                    #.pack()也可以直接放這 如果只有一行的話
#label->scale裡不能用"text"
#length->表示可滑動的範圍
#orient->垂直滑動(VERTICAL)或水平滑動(HORIZONTAL) 一定要全部大寫
#tickinterval->數值顯示區間 從from到to要拆成幾等分
#from_ ->一定要加底線,不然from是另一種參數(區分用)
#resolution->要顯示小數點後多少位 EX:resolution=0.001 就是顯示到小數後三位
#showvalue->是否要顯示出目前所指到的位置 0:false 1:true
#command->scale的數值會有默認功能, 也就是會有傳入值

#scaleShow.pack() 參考上方

window.mainloop()