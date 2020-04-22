# -*- encoding: utf-8 -*-
'''
@File : homework3.5.py
@Time : 2020/03/31 17:38:31
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
song1 = open('Blowing in the wind(1).txt','a',encoding='UTF8')
song1.write('\n1962 by Warner Bros. Inc.')
song1.close()
song1 = open('Blowing in the wind(1).txt','r',encoding='UTF8')
song2 = open('Blowing in the wind.txt','a',encoding='UTF8')
song2.write('Blowin in the wind\nBob Dylan\n')
song2.write(song1.read())
song1.close()
song2.close()
song2 = open('Blowing in the wind.txt','r',encoding='UTF8')
print(song2.read())
song2.close()
