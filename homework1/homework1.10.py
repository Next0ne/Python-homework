# -*- encoding: utf-8 -*-
'''
@File : homework1.10.py
@Time : 2020/03/06 13:36:15
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
text = input("请输入一段英文文本：")
textlist = text.split( )
record = {}
for i in range(0,len(textlist)):
    if textlist[i] in record:
        record[textlist[i]] =  record[textlist[i]] + 1
    else:
        record[textlist[i]] = 1
print(sorted(record.items(), key=lambda d:d[1], reverse = True))