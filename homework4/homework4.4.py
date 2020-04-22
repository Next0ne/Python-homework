# -*- encoding: utf-8 -*-
'''
@File : homework4.4.py
@Time : 2020/04/08 16:51:48
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import hashlib
f = open(r"D:\vscode\python\homework4.3.txt","r")
h = hashlib. sha256()
line = f.readline()
L = []
while line:
    L.append(line)
    line = f.readline()
L = L[1:6]
L1 = []
temp1 = L[0].strip().split("         ")
L1. append(temp1)
temp2 = L[1].strip().split("         ")
L1. append(temp2)
temp3 = L[2].strip().split("         ")
L. append(temp3)
temp4 = L[3].strip().split("         ")
L1. append(temp4)
temp5 = L[4].strip().split("         ")
L1. append(temp5)
print(L1)
name = input("请输入您的姓名: ")
for i in L1:
    if name in i:
        username = input("请输入您的账号: ")
        if username in i:
            password = input("请输入您的密码:")
            h.update(bytes(password, encoding='utf-8' ))
            password1 = h.hexdigest()
            if password1 in i:
                print("登陆成功! ")
            else:
                print(password1)
                print("您输入的密码不正确，登陆失败! ")
        else:
            print("您输入的账号不正确，登陆失败!")
    else:
        continue