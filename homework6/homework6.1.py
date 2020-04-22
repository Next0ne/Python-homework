# -*- encoding: utf-8 -*-
'''
@File : homework6.1.py
@Time : 2020/04/11 11:21:36
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
class dog:
    proper = [{'颜色':'白色','数量':5,'价格':'200元'},{'颜色':'黑色','数量':10,'价格':'150元'},{'颜色':'黄色','数量':6,'价格':'300元'}]
    def deal(self,color):
        for i in range(0,3):
            if self.proper[i]['颜色'] == color:
                self.proper[i]['数量'] -= 1
Dog = dog()
Dog.deal('白色')
Dog.deal('白色')
Dog.deal('白色')
for i in range(0,3):
    print(Dog.proper[i]['颜色'],"狗还有",Dog.proper[i]['数量'],"只")
    