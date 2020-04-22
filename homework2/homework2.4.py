# -*- encoding: utf-8 -*-
'''
@File : homework2.4.py
@Time : 2020/03/08 19:54:11
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# def judge( x ):
#     num = 0
#     letter = 0
#     space = 0
#     other = 0
#     for i in range(0,len(x)):
#         if ((x[i]>='A' and x[i]<='Z')or(x[i]>='a' and x[i]<='z')):
#             letter = letter + 1
#         elif (x[i] >= '0' and x[i] <= '9'):
#             num = num + 1
#         elif x[i] == ' ':
#             space = space + 1
#         else:
#             other = other + 1
#     print("数字有：",num,"个")
#     print("字母有：",letter,"个")
#     print("空格有：",space,"个")
#     print("其他字符有：",other,"个")
# str1 = input("请输入字符串：")
# list1 = list(str1)
# # print(list1)
# judge(list1)

def judge( x ):
    num = 0
    letter = 0
    space = 0
    other = 0
    for i in x:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            letter += 1
        elif i.isspace():
            space += 1
        else:
            other += 1
    print("数字有：",num,"个")
    print("字母有：",letter,"个")
    print("空格有：",space,"个")
    print("其他字符有：",other,"个")
str1 = input("请输入字符串：")
judge(str1)
        