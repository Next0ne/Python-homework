# -*- encoding: utf-8 -*-
'''
@File : homework2.7.py
@Time : 2020/03/09 17:24:57
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
from random import randint
def stu( L ):
    G = []
    for i in range(0,len(L)):
        if L[i] >= 90:
            G.append('A')
        elif L[i] >= 80 and L[i] < 90:
            G.append('B')
        elif L[i] >= 70 and L[i] < 80:
            G.append('C')
        elif L[i] < 70:
            G.append('D')
    return G
s = []
for i in range(0,10):
    s.append(randint(0,101))
print("学生的成绩为：",s)
print("等级为:",stu( s ))
    