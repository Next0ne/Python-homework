# -*- encoding: utf-8 -*-
'''
@File : homework9.2.py
@Time : 2020/05/12 19:41:41
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''


# 1 将“网络编程”章节中课件中的例子，在本机测试运行；下载安装网络编程调试工具；

# 2 编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出；

# 3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；

# 4 设计一款能实现多人聊天的系统：使用socket和多线程技术，编写全多人聊天室；
#   参考文档：https://blog.csdn.net/CxsGhost/article/details/103319864

from socket import *

def main():
   # 绑定端口信息
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    
    local_addr=('',9999)

    udp_socket.bind(local_addr)
   # 接收数据
    recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
   # 打印显示接收到的数据
    print(recv_data)

    print(recv_data[0].decode('gbk'))
    print(recv_data[1])

   # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()