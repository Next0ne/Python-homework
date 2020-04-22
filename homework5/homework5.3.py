# -*- encoding: utf-8 -*-
'''
@File : homework5.3.py
@Time : 2020/04/10 17:01:23
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
def login(func):
    username = ['1','2','3']
    password = ['123','456','789']
    def realize(*args):
        username1 = input("请输入账号:")
        if username1 in username:
            index = username.index(username1)
            password1 = input("请输入密码:")
            if password[index] == password1:
                func(*args)
            else:
                print("密码错误！")
        else:
            print("账号不存在！")
    return realize
def size(file_dir):     #用到的测试函数是homework4.7.py中的函数
    S = 0
    for f in os.listdir(file_dir):
        fsize = os.path.getsize(f)
        S = S + fsize
    print("该文件夹里的文件共 %d K" %(S))
file_dir = r'D:\vscode\python'
record = login(size)
record(file_dir)