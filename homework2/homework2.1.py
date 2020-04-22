# -*- encoding: utf-8 -*-
'''
@File : homework2.1.py
@Time : 2020/03/08 17:58:44
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def judge( x ):
    return len(x)
a = [1,2,3,4,5]
b = (1,2,3,4)
c = 'aoi'
print("列表a的长度为：",judge(a))
print("元组b的长度为：",judge(b))
print("字符串c的长度为：",judge(c))