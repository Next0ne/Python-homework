# -*- encoding: utf-8 -*-
'''
@File : person.py
@Time : 2020/04/17 11:17:25
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
class person:
    def __init__(self):
        self.ATK = 10
        self.health = 100
    def be_attacked(self,dog):
        self.health -= dog.ATK
        self.ATK -= 2
