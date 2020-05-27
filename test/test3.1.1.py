# -*- encoding: utf-8 -*-
'''
@File : test3.1.1.py
@Time : 2020/04/08 09:13:27
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

class Dog:
    count = 0
    def __init__(self,color,name):
        self.c = color
        self.n = name
        Dog.count = Dog.count + 1
    def bark(self):
        print("%s狗在叫" %(self.c))
    @staticmethod
    def num():
        print("实例化了%d条狗" %(Dog.count))
dog1 = Dog('white','bai')
dog2 = Dog('black','hei')
dog3 = Dog('yellow','huang')
Dog.num()