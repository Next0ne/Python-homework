# -*- encoding: utf-8 -*-
'''
@File : homework1.5.py
@Time : 2020/03/06 11:51:10
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
from random import randint
L = [randint(-100,100) for _ in range(10)]
print(L)
T = tuple([randint(-100,100) for _ in range(10)])
print(T)