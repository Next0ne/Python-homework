# -*- encoding: utf-8 -*-
'''
@File : test2.1.py
@Time : 2020/04/01 08:33:36
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def jia(x,y):
    print(x+y)
def jian(x,y):
    print(x-y)
def cheng(x,y):
    print(x*y)
def chu(x,y):
    print(x/y)
def calculate(x,y,func):
    func(x,y)
x = int(input('输入第一个数：'))
y = int(input('输入第二个数：'))
z = input('输入运算方法：')
if z == '+':
    calculate(x,y,jia)
elif z == '-':
    calculate(x,y,jian)
elif z == '*':
    calculate(x,y,cheng)
elif z == '/':
    calculate(x,y,chu)

        
