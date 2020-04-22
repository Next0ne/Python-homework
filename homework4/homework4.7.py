# -*- encoding: utf-8 -*-
'''
@File : homework4.7.py
@Time : 2020/04/09 18:07:04
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
def size(file_dir):
    S = 0
    for f in os.listdir(file_dir):
        fsize = os.path.getsize(f)
        S = S + fsize
    return S
file_dir = r'D:\vscode\python'
print("该文件夹里的文件共",size(file_dir),"K")