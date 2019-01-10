# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:23:47 2019

@author: chenmth
"""

import tkinter as tk

window = tk.Tk()
window.title('Frame Test')
window.geometry('600x600')

blank_frame = tk.Frame(window, width=200,height=600)
blank_frame.pack_propagate(False) 
blank_frame.grid(column=0, row=0, rowspan=2)

yellow_frame = tk.Frame(window, bg='yellow', width=200,height=600)
yellow_frame.pack_propagate(False) # stops label shrinking when it gets a label in it
yellow_frame.grid(column=1, row=0, rowspan=2)

green_frame = tk.Frame(window, bg='green', width=200,height=300)
green_frame.pack_propagate(False)
green_frame.grid(column=2, row=0)

blue_frame = tk.Frame(window, bg='blue', width=200,height=300)
blue_frame.pack_propagate(False)
blue_frame.grid(column=2, row=1)


yellow_label = tk.Label(yellow_frame, text='In the left side of yellow frame',  bg='pink')
yellow_label.pack(side='left')

green_label = tk.Label(green_frame, text='Inside the green frame',  bg='brown')
green_label.pack(side='left')

green_label = tk.Label(blue_frame, text='Inside the blue frame',  bg='brown')
green_label.pack(side='left')

left_side_label = tk.Label(blank_frame, text='In the left side of the window',  bg='red')
left_side_label.pack(side='left')

window.mainloop()