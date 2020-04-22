# -*- encoding: utf-8 -*-
'''
@File : homework2.3.py
@Time : 2020/03/08 19:43:28
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
from random import randint
def odd( L ):
    for i in range(0,len(L)):
        if int(L[i]) % 2 != 0:
            print(int(L[i]),end=" ")
xlist = [randint(0,101) for i in range(0,11)]
print("该列表里的奇数有：")
odd( xlist )