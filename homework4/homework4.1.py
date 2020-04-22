# -*- encoding: utf-8 -*-
'''
@File : homework4.1.py
@Time : 2020/04/08 15:25:43
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
from collections import deque
import datetime
def L_time():
    List = ['a'',b','c','d','e','f','g','h','i','j']
    t1 = datetime.datetime.now()
    List.insert(0,'0')
    List.append('1')
    t2 = datetime.datetime.now()
    return (t2 - t1).total_seconds()
def deque_time():
    List = ['a'',b','c','d','e','f','g','h','i','j']
    queue = deque(List)
    t1 = datetime.datetime.now()
    queue.appendleft('0')
    queue.append('1')
    t2 = datetime.datetime.now()
    return (t2 - t1).total_seconds()
Ltime = L_time()
Qtime = deque_time()
print("列表实现头尾插入用了",Ltime)
print("队列实现头尾插入用了",Qtime)
print("这两种方法时间差为",abs(Ltime - Qtime))