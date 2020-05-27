# -*- encoding: utf-8 -*-
'''
@File : test1.7.py
@Time : 2020/02/29 11:26:51
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
stu = {'学号':'120181080417','姓名':'sunh','班级':'软件1801班','年龄':'20岁'}
del stu['年龄']
print("删除后字典为：",stu)
stu['性别']='男'
print("添加后的字典为：",stu)
stu['学号']='0417'
print("更新后的字典为:",stu)