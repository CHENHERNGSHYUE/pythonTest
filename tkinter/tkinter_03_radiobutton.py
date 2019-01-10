# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:19:47 2019

@author: chenmth
"""

import tkinter as tk

window = tk.Tk()
window.title('radiobutton test')
window.geometry('600x600')

var=tk.StringVar()

labelShow = tk.Label(window, width=50, height=10, bg='yellow', text='待選擇')
labelShow.pack()

def selected():
    labelShow.config(text=var.get()+' 被選擇了~變色!')
    if(var.get()=='粉紅色'):
        labelShow.config(bg='pink') #config可以變更原本設定好的參數
    elif(var.get()=='咖啡色'):
        labelShow.config(bg='brown')
    else:
        labelShow.config(bg='green')

radioButton1 = tk.Radiobutton(window, text=1, width=20, variable=var, 
                              value='粉紅色',command=selected)
#把value的變數存到varible內給別人呼叫
radioButton1.pack()

radioButton2 = tk.Radiobutton(window, text=2, width=20, variable=var, 
                              value='咖啡色',command=selected)
radioButton2.pack()

radioButton3 = tk.Radiobutton(window, text=3, width=20, variable=var, 
                              value='綠色',command=selected)
radioButton3.pack()

window.mainloop()