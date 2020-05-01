# -*- encoding: utf-8 -*-
'''
@File : homework8.4.py
@Time : 2020/05/01 14:18:31
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''
# 多进程通讯：
#   编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息；
from multiprocessing import Process,Queue
import os,time,random

def write(q,value):
    print('发送信息进程号 %s' % os.getpid())
    print("你已发送了信息： %s"%value)
    q.put(value)
    time.sleep(random.random())

def read(q):
    print('阅读信息进程号： %s' % os.getpid())
    while True:
        if not q.empty():
            value = q.get(True)
            print('你接受到信息：  %s.' % value)
            time.sleep(random.random())
        else:
            break

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    value = input("请输入您要发送的信息：")
    while value:
        pw = Process(target=write, args=(q,value))
        pr = Process(target=read, args=(q,))
        pw.start()
        pw.join()
        pr.start()
        pr.join()
        pr.terminate()
        value = input("请输入您要发送的信息：")
    
    