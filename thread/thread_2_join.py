# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:27:54 2019

@author: chenmth
"""

import threading as thread
import time

def getA():
    for i in range(3):
        time.sleep(1) #給執行下一個任務前要停多久
        print('A')
    print(thread.current_thread())   
def getB():
    for i in range(10):
        print('B')
        
def main():
    thread1 = thread.Thread(target=getA, name='線程名字叫~A')
    thread1.start()
    thread1.join() #等此線程做完才能做下一個線程
    thread2 = thread.Thread(target=getB, name='線程名字叫~B')
    thread2.start()
    for i in range(10):
        print('main')    
main()