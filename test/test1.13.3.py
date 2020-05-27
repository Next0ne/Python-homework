# -*- encoding: utf-8 -*-
'''
@File : test1.13.3.py
@Time : 2020/03/06 09:18:14
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# res = filter(lambda x: x%2==0, lis1) #返回偶数
# print(list(res))
L = [x for x in range(1,21)]
res = filter(lambda x: (x+1)%2 == 0,L)
print(list(res))