# -*- encoding: utf-8 -*-
'''
@File : homework2.10.py
@Time : 2020/03/10 17:41:20
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def caculator( equality ):
    x = int(equality[0])
    y = int(equality[2])
    if equality[1] == '+':
        return x + y
    elif equality[1] == '-':
        return x - y
    elif equality[1] == '*':
        return x * y
    elif equality[1] == '/':
        return x / y
x = input("请输入两个数的运算：")
print( x,'=',end=' ' )
print(caculator( x ))
