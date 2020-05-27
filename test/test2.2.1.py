# -*- encoding: utf-8 -*-
'''
@File : test2.2.1.py
@Time : 2020/04/03 08:38:33
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def createCounter(): 
    i = 0
    def counter():
        nonlocal i
        i += 1
        return i
    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')