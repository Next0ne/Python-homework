# -*- encoding: utf-8 -*-
'''
@File : homework2.2.py
@Time : 2020/03/08 19:36:42
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def sum( L ):
    num = 0
    for i in range(0,len(L)):
        num = num + int(L[i])
    return num
x = input("请输入若干个数字（以空格隔开）:")
xlist = x.split( )
print( "这若干个数和为：",sum(xlist) )