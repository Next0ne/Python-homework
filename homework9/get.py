# -*- encoding: utf-8 -*-
'''
@File : get.py
@Time : 2020/05/12 20:02:25
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

#   homework9.4.py中用到的自己编的模块
import socket
import datetime


def get_ip():
    """用来搞到IP"""
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return ip


def get_time():
    """得到发送时间"""
    now = datetime.datetime.now()
    send_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return send_time