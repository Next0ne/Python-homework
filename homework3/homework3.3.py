# -*- encoding: utf-8 -*-
'''
@File : homework3.3.py
@Time : 2020/03/25 21:55:04
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def Grade_Order( file,Num,Name,G ):
    for each_line in file:
        [num,name,grade] = each_line.split(' ',2)
        Num.append(num)
        Name.append(name)
        G.append(grade)
    for i in range(0,len(G)):
        for j in range(i,len(G)):
            if G[i]<G[j]:
                tmp = G[i]
                G[i] = G[j]
                G[j] = tmp
                tmp = Num[i]
                Num[i] = Num[j]
                Num[j] = tmp
                tmp = Name[i]
                Name[i] = Name[j]
                Name[j] = tmp
file = open('stuGrade.txt','r',encoding='UTF8')
G = []
Num = []
Name = []
Grade_Order(file,Num,Name,G)
file.close()
for i in range(0,len(G)):
    print(Num[i] +' '+Name[i] +' '+G[i])