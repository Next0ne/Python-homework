# -*- encoding: utf-8 -*-
'''
@File : homework5.2.py
@Time : 2020/04/10 16:53:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import datetime
import os
def out(func):
    def inner(*args):
        print("该函数开始调用时间为",datetime.datetime.now())
        func(*args)
        print("该函数结束调用时间为",datetime.datetime.now())
    return inner
@out
def size(file_dir):     #用到的测试函数是homework4.7.py中的函数
    S = 0
    for f in os.listdir(file_dir):
        fsize = os.path.getsize(f)
        S = S + fsize
    return S
file_dir = r'D:\vscode\python'
size(file_dir)
