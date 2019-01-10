# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:09:40 2019

@author: chenmth
"""

import tkinter as tk

window = tk.Tk()
window.title('menu test')
window.geometry('450x450')

labelShow = tk.Label(window, text="A", bg='pink', width=20, height=10)
labelShow.pack()

def doNumber():
    labelShow.config(text="it is number")

def doWord():
    labelShow.config(text="it is word")
    
def doSmallWord():
    labelShow.config(text="it is small word")
    
menuShow = tk.Menu(window)

numberMenu = tk.Menu(menuShow,tearoff=1) #tearoff=1會新增一個可開啟小視窗的功能
menuShow.add_cascade(label='number', menu=numberMenu)
numberMenu.add_command(label='1',command=doNumber)
numberMenu.add_command(label='2',command=doNumber)
numberMenu.add_command(label='3',command=doNumber)
numberMenu.add_separator()
numberMenu.add_command(label='leave',command=window.quit)#quit有bug

wordMenu = tk.Menu(menuShow,tearoff=0)
menuShow.add_cascade(label='word', menu=wordMenu)
wordMenu.add_command(label='A',command=doWord)
wordMenu.add_command(label='B',command=doWord)
wordMenu.add_command(label='C',command=doWord)
wordMenu.add_separator()

extraMenu = tk.Menu(wordMenu,tearoff=0)
wordMenu.add_cascade(label='small word', menu=extraMenu)
extraMenu.add_command(label='x',command=doSmallWord)
extraMenu.add_command(label='y',command=doSmallWord)
extraMenu.add_command(label='z',command=doSmallWord)

wordMenu.add_command(label='leave',command=window.destroy)#用destoy不會當機


window.config(menu=menuShow) #在window上做顯示

window.mainloop()