# -*- encoding: utf-8 -*-
'''
@File : test2.2.2.py
@Time : 2020/04/03 09:39:51
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def memory(func):
    def inner(x,y):
        print("加法被运行了！结果为")
        func(x,y)
    return inner
def jia(x,y):
    print(x+y)
jia = memory(jia)
jia(1,2)