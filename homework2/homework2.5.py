# -*- encoding: utf-8 -*-
'''
@File : homework2.5.py
@Time : 2020/03/08 20:17:56
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# def fun1(n):
#     for i,m in n.items():
#         m = str(m)
#         if len(m) > 2:
#             n[i] = m[0:2]
#     print(n)
def Long( dic ):
    for k,v in dic.items():
        v = str( v )           #将values中所有数据类型转换成字符串类型
        if len( v ) > 2:
            dic[k] = v[0:2]
    return dic
x = {'姓名':'孙','班级':'软件1801','学号':'120181080417'}
print(Long( x ))


    