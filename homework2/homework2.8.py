# -*- encoding: utf-8 -*-
'''
@File : homework2.8.py
@Time : 2020/03/09 17:33:42
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
from collections import Counter
def count( str1 ):
    slist = list(str1)
    return Counter(slist).most_common (1)
x = input("请输入任意字符串:")
print(count(x))