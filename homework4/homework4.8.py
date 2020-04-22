# -*- encoding: utf-8 -*-
'''
@File : homework4.8.py
@Time : 2020/04/09 18:11:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import random

def create_ip(filename):
    ip = ['172.25.254.' + str(i) for i in range(1,255)]
    with open(filename,'a') as f:
        for i in range(1200):
            f.write(random.sample(ip,1)[0] + '\n')
create_ip('ip.txt')

def sorted_by_ip(filename,count=10):
    ips_dict = dict()
    with open(filename) as f:
        for ip in f:
            ip = ip.strip()
            if ip in ips_dict:
                ips_dict[ip] += 1
            else:
                ips_dict[ip] = 1
    sorted_ip = sorted(ips_dict.items(),key=lambda x:x[1],reverse=True)[:count]

    return sorted_ip

print(sorted_by_ip('ip.txt'))
