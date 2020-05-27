# -*- encoding: utf-8 -*-
'''
@File : test1.3.py
@Time : 2020/02/29 10:53:26
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
str1 = 'abcdef'
str2 = 'de'
str3 = '123'
print( "字符串str2在str1中的位置为:",str1.find(str2) )
str1.replace(str1,str2 )
print( "当前字符串str1为：",str1 )
print( "str1的长度为:",len( str1 ))