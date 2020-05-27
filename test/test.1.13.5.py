# -*- encoding: utf-8 -*-
'''
@File : test.1.13.5.py
@Time : 2020/03/13 08:28:01
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
G = [('1号',85),('2号',96),('3号',65),('4号',63),('5号',73),('6号',77),
('8号',91),('9号',75),('10号',66)]
print("十个同学的姓名，成绩为：",G)
G.sort(key = lambda k:k[1])
print("排序后信息为：",G)