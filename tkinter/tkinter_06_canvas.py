# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 14:05:21 2019

@author: chenmth
"""

import tkinter as tk

window = tk.Tk()
window.title('canvas test')
window.geometry('600x600')
imageTest=tk.PhotoImage(file='python_1.gif')

canvasShow = tk.Canvas(window, width=600, height=400, bg='pink')

image = canvasShow.create_image(0, 0, anchor='nw', image=imageTest)
#anchor->鉚釘的意思, 把鉚釘丁在(0,0)的位置, 有點bug...
x1,y1,x2,y2 = 350,100,550,370
rectangleShow = canvasShow.create_rectangle(x1,y1,x2,y2,fill='blue')
#(x1,y1,x2,y2) fill填滿顏色
#width=絕對值(x2-x1), y同理
ovalShow = canvasShow.create_oval(x1,y1,x2,y2,fill='brown')
#center=((x1+x2)/2,(y1+y2)/2) and 寬=絕對值(x2-x1), y同理
lineShow = canvasShow.create_line(x1,y1,x2,y2,fill='yellow',width=6)
#width表示線的寬度
arc = canvasShow.create_arc(x1,y1,x2,y2,fill='pink',width=1, 
                            start=0, extent=45)
#center=((x1+x2)/2,(y1+y2)/2) radius=絕對值(x2-x1)/2
#start to extent ->角度從幾度然後展開幾度(逆時針) arc表示弧形
canvasShow.pack() #canvas迴圈結束

def moveDown():
    canvasShow.move(rectangleShow,0,20)

def moveUp():
    canvasShow.move(rectangleShow,0,-20)
    
buttonShow = tk.Button(window, width=50, text='往下移動',
                       command=moveDown).pack()

buttonShow2 = tk.Button(window, width=50, text='往上移動',
                       command=moveUp).pack()

window.mainloop()