# -*- encoding: utf-8 -*-
'''
@File : homework4.3.py
@Time : 2020/04/08 16:29:32
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import hashlib
f = open(r"D:\vscode\python\homework4.3.txt","w")
h = hashlib. sha256()
num = 0
while num < 5:
    name = input("请输入第" + str(num + 1) + "个同学的姓名:")
    username = input("请输入账号: ")
    password = input("请输 入密码:")
    h.update(bytes(password, encoding= 'utf-8' ))
    password1 = h. hexdigest()
    if num == 0:
        f.writelines("姓名         账号         密码(已加密)" + '\n')
    temp = name + '         ' + username + '         ' + password1
    f.writelines(temp + '\n')
    num += 1
