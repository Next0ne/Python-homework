# -*- encoding: utf-8 -*-
'''
@File : homework3.1.py
@Time : 2020/03/25 20:30:45
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def input_L():
    L = []
    while True:
        s = input("请输入文字信息：")
        if s == ' ':
            return L
        L.append(s)

def write_file(L):
    try:
        f = open(r"D:\vscode\python\input.txt","w",encoding='UTF8')
        for x in L:
            f.write(x)
            f.write("\n")
        f.close()
    except IOError:
        print("write error;")

write_file(input_L())
