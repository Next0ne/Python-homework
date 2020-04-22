# -*- encoding: utf-8 -*-
'''
@File : homework1.6.py
@Time : 2020/03/06 12:56:33
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
num = [1,1]
for i in range(2,999):
    if num[i-1] + num[i-2] <= 100:
        num.append(num[i-1] + num[i-2])
    else:
        break
print("100以内的斐波那契数列为：",num)
