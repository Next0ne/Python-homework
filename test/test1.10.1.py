# -*- encoding: utf-8 -*-
'''
@File : test1.10.1.py
@Time : 2020/03/04 08:18:47
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

x = input( "请输入： " )
xlist = x.split(",")
print( "转换成列表后为： ",xlist)
xtup = tuple(xlist)
print( "转换成元组后为： ",xtup)
