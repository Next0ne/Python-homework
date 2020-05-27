# -*- encoding: utf-8 -*-
'''
@File : test1.17.3.py
@Time : 2020/03/18 09:27:55
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

import os

# print("当前工作路径为：",os.getcwd())
with open('D:/vscode/python/test/test1.17.3.py.txt','r',encoding='utf8') as f:
    for i in f.readlines():
        print( i.strip() )