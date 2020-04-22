# -*- encoding: utf-8 -*-
'''
@File : homework5.4.py
@Time : 2020/04/10 19:33:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

def log1(func):
    def inner1():
        func()
    return inner1
def log2(func):
    def inner2(x):
        func(x)
    return inner2
def log3(func):
    def inner3():
        res = func()
        print(res) 
    return inner3
    
@log1
def target_function1():
    print("打印输出20000之内的素数:")
    for n in range(2, 100):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            print(n,end=' ')
    print('\n')

@log2
def target_function2(x):
    print("计算整数2-M之间的素数:")
    for n in range(2, x):
        for j in range(2, n):
            if n % j == 0:
                break
        else:
            print(n,end=' ')
    print('\n')

@log3
def target_function3():
    print("计算整数2-10000之间的素数的个数:")
    num = 0
    for n in range(2, 100):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            num += 1
    return num

target_function1()
target_function2(int(input("输入M：")))
target_function3()
