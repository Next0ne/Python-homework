# -*- encoding: utf-8 -*-
'''
@File : homework6.2.py
@Time : 2020/04/11 11:54:36
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
class student:
    def __init__(self,name,age,score_Chinese,score_Math,score_English):
        self.name = name 
        self.age = age
        self.score_Chinese = score_Chinese
        self.score_English = score_English
        self.score_Math = score_Math
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        max = 0
        if self.score_Chinese > self.score_English:
            max = self.score_Chinese
        else:
            max = self.score_English
        if max < self.score_Math:
            max = self.score_Math
        return max
student1 = student('张三',18,90,80,70)
student2 = student('李四',20,95,85,75)
print(student1.get_name())
print(student1.get_age())
print(student2.get_course())
            