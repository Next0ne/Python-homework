# -*- encoding: utf-8 -*-
'''
@File : test1.11.1.py
@Time : 2020/03/04 09:10:22
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

a = [0,1,2,3,4,5,6,7,8,9]
for i in range(len(a)):
    print( a[i],end=' ' )
print( "其中偶数有：")
for j in range(len(a)):
    if j%2 == 0:
        print( a[j],end= ' ' )

      