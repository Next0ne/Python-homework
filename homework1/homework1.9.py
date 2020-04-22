# -*- encoding: utf-8 -*-
'''
@File : homework1.9.py
@Time : 2020/03/06 13:28:45
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
from random import randint
x = randint(0,10)
for i in range(0,3):
    y = int(input("请输入一个10以内的正数："))
    if(x == y):
        print("猜对了！")
        break
    else:
        print("猜错了！")
        if i == 2:
            print ("你输了！")
            print ("这个数字为",x)
            break
