# -*- encoding: utf-8 -*-
'''
@File : homework1.2.py
@Time : 2020/03/06 11:10:53
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
dict = {'0401':60,'0402':95,'0403':82,'0404':75,'0405':62,'0406':86,
'0407':82,'0408':72,'0409':86,'0410':94}
for k,v in dict.items():
    if dict[k] >= 80:
        print(k,":",v)