# -*- encoding: utf-8 -*-
'''
@File : test1.13.2.py
@Time : 2020/03/06 08:33:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def changelist( L ):
    print("传参之前列表的值：",L)
    L.append([4,5,6])
    return( L )

L = [1,2,3]
print ("传参之前列表的地址：",id( L ))
L1 = changelist( L )
print ("传参之后列表的地址：",id( L1 ))


