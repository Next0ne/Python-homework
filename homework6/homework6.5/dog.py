# -*- encoding: utf-8 -*-
'''
@File : homework6.5.py
@Time : 2020/04/17 11:07:43
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
class dog:
    def __init__(self):
        self.ATK = 15
        self.health = 80
    def be_attacked(self,person):
        self.health -= person.ATK
        self.ATK -= 3
