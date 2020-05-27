# -*- encoding: utf-8 -*-
'''
@File : test1.13.1.py
@Time : 2020/03/06 08:13:19
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

def sum( weight,price ):
    return weight*price

w = int(input( "请输入购买苹果的重量：" ))
p = int(input( "请输入购买苹果的单价：" ))
print( "共需付%d元" %(sum(w,p)))