# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:15:11 2019

@author: chenmth
"""

import threading

def thread6():
    print("test is %s" %threading.current_thread()) #類似java printf的%s 只是後面用%區分
    print(threading.current_thread())
def main():
    newThread = threading.Thread(target=thread6, name='six')
    newThread.start()
    print('\n'+str(threading.active_count())) #顯示線程數量
    print(threading.current_thread()) #顯示目前的線程位置(執行緒位置)
    #print(threading.enumerate()) #列出(enumerate所有線程名稱(使用到的)

main()