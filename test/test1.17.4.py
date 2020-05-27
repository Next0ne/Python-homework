# -*- encoding: utf-8 -*-
'''
@File : test1.17.4.py
@Time : 2020/03/18 09:51:26
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
L = []
with open('D:/vscode/python/test/test1.17.3.py.txt','r',encoding='utf8') as f:
    for i in f.readlines():
        L[i] = i.strip()