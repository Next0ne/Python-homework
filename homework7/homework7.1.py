# -*- encoding: utf-8 -*-
'''
@File : homework7.1.py
@Time : 2020/04/29 15:45:34
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件;提示，文件有1000行，注意控制每次读取的行数；
import re
rule = re.compile(r"http://[a-zA-Z0-9\.\-\_]{0,25}")
with open(r"D:\vscode\python\webspiderUrl.txt", "r", encoding="utf-8") as f1:
    with open(r"D:\vscode\python\webspiderUrl(1).txt", "w") as f2:
        for line in f1:
            all_match = rule.findall(line)
            for rec in all_match:
                f2.write(rec)
                f2.write("\n")