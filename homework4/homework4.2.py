# -*- encoding: utf-8 -*-
'''
@File : homework4.2.py
@Time : 2020/04/08 16:07:51
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import datetime
def transform(t):
    T = datetime.datetime.strptime(t,'%Y-%m-%d')
    t_tuple = T.date().isocalendar()
    week = t_tuple[1] - 7
    print("这天为第%d周，周%d" %(week,t_tuple[2]))
t = input("请输入任意日期（格式为：年-月-日）")
transform(t)
