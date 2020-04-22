# -*- encoding: utf-8 -*-
'''
@File : homework1.3.py
@Time : 2020/03/06 11:40:26
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
L1 = [1,2,5,6]
L2 = [x for x in range(0,11)]
print ("两个列表中相同元素有：")
for x in range(0,len(L1)):
    for y in range(0,len(L2)):
        if L1[x] == L2[y]:
            print( L1[x] ) 