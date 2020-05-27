# -*- encoding: utf-8 -*-
'''
@File : test1.8.py
@Time : 2020/02/29 11:31:13
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
basket1={'one','two','three','four'}
basket2=set(("one","two","three"))
basket1.add("five")
print("添加后的集合basket1为：",basket1)
basket2.remove("three")
print("删除后的集合basket2为：",basket2)
print(basket1 - basket2)
print(basket1|basket2)
print(basket1 & basket2)