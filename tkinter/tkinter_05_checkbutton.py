# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 13:31:56 2019

@author: chenmth
"""

import tkinter as tk

window = tk.Tk()
window.title('Scale Test')
window.geometry('500x500') 

object1 = tk.Label(window, text='No select', bg='yellow', font=('Times New Roman',30),
                   width=50, height=5) #width和height限制為int形式
object1.pack()

var1 = tk.IntVar() #若想用文字顯示可以改成StringVar()
var2 = tk.IntVar() #checkbutton用sting會有第一次顯示bug所以用數字

def result():
    if(var1.get()==0) & (var2.get()==0):
        object1.config(text='I hate fruit')
    elif(var1.get()==0) & (var2.get()==1):
        object1.config(text='I only love banana')
    elif(var1.get()==1) & (var2.get()==0):
        object1.config(text='I only love apple')
    else:
        object1.config(text='I love apple and banana')
        
checkbuttonShow1 = tk.Checkbutton(window, text='Apple', font=('Arial',22),
                                  variable=var1, onvalue=1, offvalue=0, 
                                  command=result)
#onvalue和offvalue的值可以隨意設定,也可以是int也可以是str
checkbuttonShow1.pack()

checkbuttonShow2 = tk.Checkbutton(window, text='Banana', font=('Arial',22),
                                  variable=var2, onvalue=1, offvalue=0, 
                                  command=result)
checkbuttonShow2.pack()

window.mainloop()