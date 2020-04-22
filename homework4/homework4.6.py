# -*- encoding: utf-8 -*-
'''
@File : homework4.6.py
@Time : 2020/04/08 17:26:40
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
from datetime import datetime
print("名称                  日期                    类型                  大小")
file_dir = r'D:\vscode\python'
for f in os.listdir(file_dir):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    if os.path.isdir(f):
        type = '文件夹'
    if os.path.isfile(f):
        type = '文件'
    print('%s          %s          %s          %10d' % (f,mtime,type,fsize))