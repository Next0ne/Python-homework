# -*- encoding: utf-8 -*-
'''
@File : homework3.2.py
@Time : 2020/03/25 20:49:52
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
f = open(r"D:\vscode\python\input.txt","r",encoding='UTF8')
L = []
for x in f.readlines():
    L.append( x )
for i in range(0,len(L)):
    print("#第%d行：" %(i+1),L[i])