# -*- encoding: utf-8 -*-
'''
@File : homework6.3.py
@Time : 2020/04/16 19:51:14
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
class dictclass:
    def __init__(self,out_dict):
        self.dict = out_dict
    def del_dict(self,dict_key):
        if dict_key in self.dict.keys():
            del self.dict[dict_key]
        print(self.dict)
    def get_dict(self,dict_key):
        if dict_key in self.dict:
            print(self.dict[dict_key])
        else:
            print("Not found !")
    def get_key(self):
        dlist = []
        for k,v in self.dict.items():
            dlist.append(k)
        print(dlist)
    def update_dict(self,in_dict):
        self.dict.update(in_dict)
        print(self.dict)
dict = dictclass({'Name': 'Runoob', 'Age': 7, 'Class': 'First'})
dict.get_key()
dict.get_dict('Age')
dict.del_dict('Class')
dict.update_dict({'Name': '小菜鸟'})
