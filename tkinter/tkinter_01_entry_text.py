# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:52:25 2019

@author: chenmth
"""

import tkinter as tk

window = tk.Tk()
window.title('輸入與顯示測試')
window.geometry('500x500')
    
entryMode = tk.Entry(window, width=20, show=None) #show表示輸入的顯示方式 None表示沒限制
entryMode.pack()

def insertAnywhere():
    var = entryMode.get()
    textShow.insert('insert', var)

def insertToTheEnd():
    var = entryMode.get()
    textShow.insert('end', var)
    
insertButton = tk.Button(window, text='插入文字於游標前', width=20, height=5, bg='pink',
                         command=insertAnywhere)
insertButton.pack()


insertButton2 = tk.Button(window, text='插入文字到最後', width=20, height=5, bg='pink',
                          command=insertToTheEnd)
insertButton2.pack()

textShow = tk.Text(window, height=5, width= 25)
textShow.pack()

window.mainloop()