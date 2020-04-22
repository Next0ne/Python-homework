# -*- encoding: utf-8 -*-
'''
@File : homework3.6.py
@Time : 2020/03/31 17:51:48
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
dic1 = {}
dic2 = {}
num = 0
with open('python in English1.txt','r') as f1:
    for each_line in f1:
        line_list = each_line.split(' ')
        for i in range(0,len(line_list)):
            if line_list[i] in dic1:
                dic1[line_list[i]] += 1
            else:
                dic1[line_list[i]] = 1
with open('python in English2.txt','r') as f2:
    for each_line in f2:
        line_list = each_line.split(' ')
        for i in range(0,len(line_list)):
            if line_list[i] in dic2:
                dic2[line_list[i]] += 1
            else:
                dic2[line_list[i]] = 1
word1 = sorted(dic1.items(),key = lambda item:item[1],reverse = True)   #对dic1排序，True代表从小到大
word2 = sorted(dic2.items(),key = lambda item:item[1],reverse = True) 
for i in range(0,10):
    if word1[i] == word2[i]:
        num += 1
if num == 5:
    print("相似度为50%")
elif num == 6:
    print("相似度为60%")
elif num == 7:
    print("相似度为70%")
elif num == 8:
    print("相似度为80%")
elif num == 9:
    print("相似度为90%")
elif num == 10:
    print("相似度为100%")
else:
    print("相似度不足50%")

