# -*- encoding: utf-8 -*-
'''
@File : homework2.6.py
@Time : 2020/03/09 17:08:56
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def fibo( n ):
    num = [1,1]
    for i in range(2,999):
        if num[i-1] + num[i-2] <= n:
            num.append(num[i-1] + num[i-2])
        else:
            break
    return num
x = int(input("求n以内的斐波那契额数列："))
print(fibo( x ))


