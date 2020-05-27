# -*- encoding: utf-8 -*-
'''
@File : test1.17.1.py
@Time : 2020/03/18 08:29:20
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import os
pwd = os.path.abspath('homework1.1.py')
print(pwd)
print( os.path.basename(pwd) )   # 返回文件名
print( os.path.dirname(pwd)  )  # 返回目录路径
print( os.path.split(pwd) )      # 分割文件名与路径
print( os.path.join('D','homework1','homework1.1.py') )  # 将目录和文件名合成一个路径
