# -*- encoding: utf-8 -*-
'''
@File : homework2.9.py
@Time : 2020/03/10 17:23:01
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
from random import randint
def maopao( array ):
    for i in range(0,(len(array)) - 1):
        for j in range(0,(len(array)) - 1 - i):
            if array[j] > array[j+1]:
                buf = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buf
    return array
a = [randint(0,101) for i in range(0,10)]
print( "随机10个数字(0到100)组成的数组从小到大排序为：",maopao( a ) )


