# -*- encoding: utf-8 -*-
'''
@File : homework6.4.py
@Time : 2020/04/16 20:29:35
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
class student:
    def __init__(self,name,age,sex,Chinese,Math,English):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__Chinese = Chinese
        self.__Math = Math
        self.__English = English
    def num(self):
        print("%s同学的总分为：%d分" %(self.__name,self.__Chinese+self.__Math+self.__English))
    def average(self):
        print("%s同学的平均分为：%d分" %(self.__name,(self.__Chinese+self.__Math+self.__English)/3))
    def info(self):
        print("姓名：%s,年龄：%s,性别：%s,成绩（语文，数学，英语）:%d %d %d" %(self.__name,self.__age,self.__sex,self.__Chinese,self.__Math,self.__English))
stu = student('张三',18,'男',90,80,70)
stu.num()
stu.average()
stu.info()
