# -*- encoding: utf-8 -*-
'''
@File : homework1.1.py
@Time : 2020/03/05 23:05:20
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 1 元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；

print("0 ~ 50的奇数有：")
for x in range(0,51):
    if (x + 1) % 2 == 0:
        print(x,end= " ")
print("\n")
print("偶数有：")
for x in range(0,51):
    if x % 2 == 0:
        print(x,end= " ")
print("\n")
print("质数有：")
for x in range(2,51):
    for n in range(2,x):
        if x % n == 0:
            break
    else:
        print( x,end= " " )
print("\n")
print ("能同时被2和3整除的数有：")
for x in range(2,51):
    if x % 2 == 0:
        if x % 3 == 0:
            print(x,end=" ")




