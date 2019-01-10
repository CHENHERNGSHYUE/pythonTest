# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:28:30 2019

@author: chenmth
"""

import tkinter as tk

window = tk.Tk()
window.title('listbox測試')
window.geometry('200x200')

var = tk.StringVar() #類似java的"toString"

labelShow = tk.Label(window, textvariable=var, width=5, height=5, bg='yellow')
labelShow.pack()

def insertVar():
    temp=labelList.get(labelList.curselection())
    var.set(temp)
    
button1 = tk.Button(window, text='把下丟到上', width=15, height=5, bg='pink',
                    command=insertVar)
button1.pack()

listItem = tk.StringVar()
listItem.set(['a','b','c','d'])
labelList = tk.Listbox(window, listvariable=listItem, width=10) 
labelList.pack()  

newListItem = ['aa','bb','cc']
for i in newListItem:
    labelList.insert('end',i)
labelList.insert(0,'start')
labelList.delete(1) #刪除第二行的項目 ('a')

window.mainloop()