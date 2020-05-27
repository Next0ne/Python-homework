# -*- encoding: utf-8 -*-
'''
@File : test1.13.4.py
@Time : 2020/03/06 09:41:21
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def L(x,*argues):
    print('第一个参数:', x)
    print('第二个参数:', argues)
    for i in argues:
        print('第二个参数里面的值:',i)

def T(x,**kwargues):
    print('第一个参数:', x)
    print('第二个参数:', kwargues)
    for i in kwargues:
        print('第二个参数里面的值:',i)

L(1,2,3,4,5,6)
T(2,y = 3, z = 4)


