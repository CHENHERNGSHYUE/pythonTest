# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:03:18 2019

@author: chenmth
"""

import time as t #減少輸入字數

print(t.ctime())

from time import ctime #只載入某個物件包裡的特定功能

print(ctime())

from time import* #直接輸入全部功能 "*"

print(localtime()) #也不用加包裝名稱了