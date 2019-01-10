# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:53:21 2019

@author: chenmth
"""

import tkinter as tk

window = tk.Tk()
window.title('擺放格式測試')
window.geometry('600x600')

tk.Label(window, text='pack位置下', bg='red', fg='white', font=('Arial',20),
         width=10, height=2).pack(side='bottom')
tk.Label(window, text='pack位置左', bg='red', fg='white', font=('Arial',20),
         width=10, height=2).pack(side='left')
tk.Label(window, text='pack位置右', bg='red', fg='white', font=('Arial',20),
         width=10, height=2).pack(side='right')
tk.Label(window, text='pack位置上', bg='red', fg='white', font=('Arial',20),
         width=10, height=2).pack() #pack默認top

#anchor的位置就是(x,y)的位置
tk.Label(window, text='釘左上', bg='green', fg='white', font=('Arial',10),
         width=15, height=2).place(x=300,y=300,anchor='nw') 
tk.Label(window, text='釘右上', bg='green', fg='white', font=('Arial',10),
         width=15, height=2).place(x=300,y=300,anchor='ne')
tk.Label(window, text='釘正上', bg='pink', fg='black', font=('Arial',10),
         width=8, height=2).place(x=300,y=300,anchor='n') 
tk.Label(window, text='釘左下', bg='green', fg='white', font=('Arial',10),
         width=15, height=2).place(x=300,y=300,anchor='sw') 
tk.Label(window, text='釘右下', bg='green', fg='white', font=('Arial',10),
         width=15, height=2).place(x=300,y=300,anchor='se')
tk.Label(window, text='釘正下', bg='pink', fg='black', font=('Arial',10),
         width=8, height=2).place(x=300,y=300,anchor='s')
tk.Label(window, text='釘左邊', bg='pink', fg='black', font=('Arial',10),
         width=15, height=1).place(x=300,y=300,anchor='w') 
tk.Label(window, text='釘右邊', bg='pink', fg='black', font=('Arial',10),
         width=15, height=1).place(x=300,y=300,anchor='e')
tk.Label(window, text='釘中間', bg='green', fg='white', font=('Arial',10),
         width=8, height=1).place(x=300,y=300,anchor='center')

#因grid擺放位置和pack重疊 所以另外開視窗
window2 = tk.Tk()
window2.title("grid test")
window2.geometry('500x500')
for i in range(4):
    for j in range(3):
        tk.Label(window2, text='grid擺放位置(pad)', 
                 bg='yellow').grid(row=i, column=j, padx=5, pady=10)
#xpad和ypad分別表示x和y間與間的距離
        
window.mainloop()
window2.mainloop()