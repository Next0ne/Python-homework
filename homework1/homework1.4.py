# -*- encoding: utf-8 -*-
'''
@File : homework1.4.py
@Time : 2020/03/06 11:45:25
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
year = int(input("请输入年份："))
if (year % 4 == 0 and year % 100 !=0):
    print("%d是闰年" %(year))
elif (year % 100 == 0 and year % 400 == 0):
    print("%d是闰年" %(year))
else:
    print("%d不是闰年" %(year))