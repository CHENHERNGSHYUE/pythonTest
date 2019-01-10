# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:00:12 2019

@author: chenmth
"""

import tkinter as tk

window = tk.Tk()
window.title('messagebox test')
window.geometry('600x300')

def answer():
    print(input(''))
def messageBoxShowing():
    tk.messagebox.showinfo(title='info box', message='一般顯示')
    tk.messagebox.showwarning(title='warning box', message='可執行但有問題')
    tk.messagebox.showerror(title='warning box', message='執行異常')
    
    answer = tk.messagebox.askquestion(title='question', message='回答問題')
    if(answer=='yes'): #注意 question是return yes & no
        name=input('輸入名字: ')
        age=input('輸入年齡: ')
        tk.messagebox.showinfo(title='個人資料', message=name+'今年'+age+'歲')
    else: 
        tk.Label(window, text='輸入失敗', fg='red').pack()
    
    answer = tk.messagebox.askyesno(title='小問題', message='你是人嗎?')
    if answer: #注意 yesno是return True & False
        tk.Label(window, text='正常人', fg='blue').pack()
    else:
        tk.Label(window, text='快跑喔!', fg='red', font=('Arial',50)).pack()
        
tk.Button(window, text='show new box', bg='pink', command=messageBoxShowing
          ).pack()

window.mainloop()

