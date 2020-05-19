# 设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#    使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；

import pymysql
import datetime

mydb=pymysql.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="test"
)

print("这是一个留言板！")

def menu():
    print("请输入编号来进行操作：")
    print("1.进行留言")
    print("2.删除留言")
    print("3.更新留言")
    print("4.查询所有留言")
    print("0.退出留言板")


def choic(x):
    mycursor = mydb.cursor()
    if x == 1:
        Content = input("请输入要留言的内容：")
        Name = input("请输入留言人：")
        Time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        is_delete = 0
        sql = "INSERT INTO message(ID,content,name,time,is_delete) " \
              "VALUES (0,'%s','%s','%s',%s)"% \
              (Content,Name,Time,is_delete)
        try:
            mycursor.execute(sql)
            mydb.commit()
        except:
            mydb.rollback()
        print("添加成功！")


    if x == 2:
        id = int(input("请输入留言编号："))
        sql = "UPDATE  message SET is_delete = 1 WHERE ID = %d" %(id)
        try:
            mycursor.execute(sql)
            mydb.commit()
        except:
            mydb.rollback()
        print("删除成功！")


    if x == 3:
        id = int(input("请输入留言编号："))
        Content = input("请输入要留言的内容：")
        Name = input("请输入留言人：")
        Time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql1 = "UPDATE  message SET content = '%s' WHERE ID = %d;" %(Content,id)
        sql2 = "UPDATE  message SET name = '%s' WHERE ID = %d;" %(Name,id)
        sql3 = "UPDATE  message SET time = '%s' WHERE ID = %d;" %(Time,id)
        try:
            mycursor.execute(sql1)
            mydb.commit()
            mycursor.execute(sql2)
            mydb.commit()
            mycursor.execute(sql3)
            mydb.commit()
        except:
            mydb.rollback()
        print("更新成功！")

    if x == 4:
        sql = "SELECT * FROM message"
        try:
            # 执行SQL语句
            mycursor.execute(sql)
            # 获取所有记录列表
            results = mycursor.fetchall()
            for row in results:
                ID = row[0]
                Content = row[1]
                Name = row[2]
                Time= row[3]
                is_delete = row[4]
                # 打印结果
                print("ID=%s,Content=%s,Name=%s,Time=%s,is_delete=%d" % \
                      (ID, Content, Name, Time, is_delete))
        except:
            mydb.rollback()
        print("查询成功！")


if __name__ == '__main__':
    menu()
    menu_choic = int(input("请输入0-4任意整数："))
    while(menu_choic):
        choic(menu_choic)
        menu_choic = int(input("请输入0-4任意整数："))
    else:
        print("退出留言板！")
