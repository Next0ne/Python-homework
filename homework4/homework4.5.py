# -*- encoding: utf-8 -*-
'''
@File : homework4.5.py
@Time : 2020/04/08 17:10:28
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
f1 = open(r"D:\vscode\python\homework4.5(1).txt",'r',encoding='UTF8')
f2 = open(r"D:\vscode\python\homework4.5(2).txt",'a',encoding='UTF8')
txt = []
T = ''
for line in f1:
    txt.append(line)
for i in range(0,len(txt)):
    T = T + txt[i]
f2.write(T)