# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:22:35 2019

@author: chenmth
"""

import tkinter as tk
window = tk.Tk()
window.title('frame test')
window.geometry('600x450')

label1 = tk.Label(window, text='In the left side of window', bg='red', fg='white')
label1.pack(side='left')

frameShow = tk.Frame(window, bg='yellow', width=100,height=50)
frameShow.pack()

label2 = tk.Label(frameShow, text='In the left side of yellow frame', bg='pink')
label2.pack(side='left')

subFramel = tk.Frame(frameShow, bg='green', width=200,height=200, borderwidth=2)
subFramel.pack()

label3 = tk.Label(subFramel, text='Inside the green frame', bg='brown', fg='white')
label3.pack(side='right')

subFrame2 = tk.Frame(frameShow, bg='blue', width=180,height=200, borderwidth=2)
subFrame2.pack(side='left')

label3 = tk.Label(subFrame2, text='Inside the blue frame',bg='brown', fg='white', borderwidth=2)
label3.pack()

window.mainloop()