# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:16:28 2019

@author: chenmth
"""

import tkinter as tk #GUI

window = tk.Tk() #package tkinter 裡的Tk class
window.title('First Design')
window.geometry('500x500') #geometry=> 幾何 create視窗大小 一定要用'x'不可以'*'
#('寬x高' or 'width x height')        
var = tk.StringVar()
object1 = tk.Label(window, textvariable=var, bg='yellow', font=('Times New Roman',20),
                   width=10, height=5) #放在window內 背景黃色 數字大小指的是幾個字符高度

boolean = False 
def click():
    global boolean #boolean來自global的變數
    if boolean == False:
        var.set("Bomb!!")
        boolean = True
    else:
        var.set("")
        boolean = False

object2 = tk.Button(window, text='click', bg='pink', width=10, height=5,
                    command=click)

object1.pack() #擺放位置
object2.pack() 

window.mainloop() #執行,把上面程式看成一個迴圈
