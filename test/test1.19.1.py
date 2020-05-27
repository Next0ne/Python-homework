# -*- encoding: utf-8 -*-
'''
@File : test1.19.1.py
@Time : 2020/03/25 08:41:37
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
def copy( path1,path2 ):
    f1 = open(path1,'r',encoding='UTF8')
    f = "test1.txt"
    path2 = os.path.join( path2,f )
    f2 = open(path2,'w')
    for i in f1.read():
        f2.write(i)
path1 = r'D:\a\test.txt'
path2 = r'D:\b'
copy( path1,path2 )
    