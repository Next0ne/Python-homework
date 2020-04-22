# -*- encoding: utf-8 -*-
'''
@File : homework5.1.py
@Time : 2020/04/10 16:39:54
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import time
import os
def otime(func):
    def itime(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print("该函数运行的时间为",end - start,"秒！")
    return itime
def size(file_dir):     #用到的测试函数是homework4.7.py中的函数
    S = 0
    for f in os.listdir(file_dir):
        fsize = os.path.getsize(f)
        S = S + fsize
    return S
file_dir = r'D:\vscode\python'
func = otime(size)
func(file_dir)
