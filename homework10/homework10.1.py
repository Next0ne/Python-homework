import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="test"
)

mycursor = mydb.cursor()

print("查询所有男生的姓名，年龄，所在班级名称:")
sql = open(r"D:\Pycharm\homework10\SQL\10.1.sql",'r',encoding='UTF-8').read()
mycursor.execute(sql)
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
for x in myresult:
    print(x)
print("\n")

print("查询所有查询编号小于4或没被删除的学生:")
sql = open(r"D:\Pycharm\homework10\SQL\10.2.sql",'r',encoding='UTF-8').read()
mycursor.execute(sql)
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
for x in myresult:
    print(x)
print("\n")

print("查询姓黄并且“名”是一个字的学生:")
sql = open(r"D:\Pycharm\homework10\SQL\10.3.sql",'r',encoding='UTF-8').read()
mycursor.execute(sql)
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
for x in myresult:
    print(x)
print("\n")

print("查询编号是1或3或8的学生:")
sql = open(r"D:\Pycharm\homework10\SQL\10.4.sql",'r',encoding='UTF-8').read()
mycursor.execute(sql)
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
for x in myresult:
    print(x)
print("\n")

print("查询编号为3至8的学生:")
sql = open(r"D:\Pycharm\homework10\SQL\10.5.sql",'r',encoding='UTF-8').read()
mycursor.execute(sql)
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
for x in myresult:
    print(x)
print("\n")

print("查询未删除男生信息，按年龄降序:")
sql = open(r"D:\Pycharm\homework10\SQL\10.6.sql",'r',encoding='UTF-8').read()
mycursor.execute(sql)
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
for x in myresult:
    print(x)
print("\n")

print("查询女生的总数:")
sql = open(r"D:\Pycharm\homework10\SQL\10.7.sql",'r',encoding='UTF-8').read()
mycursor.execute(sql)
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
girls_num = 0
for x in myresult:
    girls_num += 1
print(girls_num)
print("\n")

print("查询学生的平均年龄:")
sql = open(r"D:\Pycharm\homework10\SQL\10.8.sql",'r',encoding='UTF-8').read()
mycursor.execute(sql)
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
age = 0
num = 0
for x in myresult:
    age += x[0]
    num += 1
print(age/num)
print("\n")

print("分别统计性别为男/女的人年龄平均值:")
sql = open(r"D:\Pycharm\homework10\SQL\10.9男.sql",'r',encoding='UTF-8').read()
mycursor.execute(sql)
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
age = 0
num = 0
for x in myresult:
    age += x[0]
    num += 1
print("男：",age/num)

sql = open(r"D:\Pycharm\homework10\SQL\10.9女.sql",'r',encoding='UTF-8').read()
mycursor.execute(sql)
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
age = 0
num = 0
for x in myresult:
    age += x[0]
    num += 1
print("女：",age/num)
print("\n")

print("按照性别来进行人员分组显示:")
sql = open(r"D:\Pycharm\homework10\SQL\10.10男.sql",'r',encoding='UTF-8').read()
mycursor.execute(sql)
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
boys = []
for x in myresult:
    boys.append(x[0])
print("|男   |",boys)

sql = open(r"D:\Pycharm\homework10\SQL\10.10女.sql",'r',encoding='UTF-8').read()
mycursor.execute(sql)
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
girls = []
for x in myresult:
    girls.append(x[0])
print("|女   |",girls)

sql = open(r"D:\Pycharm\homework10\SQL\10.10中性.sql",'r',encoding='UTF-8').read()
mycursor.execute(sql)
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
mid_males = []
for x in myresult:
    mid_males.append(x[0])
print("|中性   |",mid_males)

sql = open(r"D:\Pycharm\homework10\SQL\10.10保密.sql",'r',encoding='UTF-8').read()
mycursor.execute(sql)
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
secret = []
for x in myresult:
    secret.append(x[0])
print("|中性   |",secret)