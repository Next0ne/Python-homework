# -*- encoding: utf-8 -*-
'''
@File : homework8.1.py
@Time : 2020/04/29 16:28:31
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# 1  有100个同学的分数：数据请用随机函数生成；
#      A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
#      B 利用线程池来实现；
import threading
from random import randint
from multiprocessing import Pool
stu = []
for i in range(100):
    stu.append(randint(0,100))
j = 0
k = 0
# # 多线程实现
# def out_student(student):
#     global stu
#     global j
#     for i in range(20):
#         mutex.acquire()
#         print("第%d个同学的成绩为：%d" %(j + 1,student[j]))
#         j += 1
#         mutex.release()
#     print("线程运行完毕！")
# if __name__ == "__main__":
#     mutex = threading.Lock()
#     th1 = threading.Thread(target=out_student,args=(stu,))
#     th1.start()
#     th2 = threading.Thread(target=out_student,args=(stu,))
#     th2.start()
#     th3 = threading.Thread(target=out_student,args=(stu,))
#     th3.start()
#     th4 = threading.Thread(target=out_student,args=(stu,))
#     th4.start()
#     th5 = threading.Thread(target=out_student,args=(stu,)) 
#     th5.start()
# 进程池实现
def out_student():
    global stu
    global k
    print("第%d个同学的成绩为：%d" %(k + 1,stu[k]))
    k += 1
if __name__ == "__main__":
    p = Pool(5)
    for i in range(0,100):
        p.apply_async(out_student)
    print("---------start--------")
    p.close()
    p.join()
    print("-----------end---------")