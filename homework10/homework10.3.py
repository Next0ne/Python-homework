# 3  设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#              用SQLAchemy模块来实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑



from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import  datetime


Base = declarative_base()
class User(Base):
    # 表的名字:
    __tablename__ = 'message'

    # 表的结构:
    ID = Column(String(20), primary_key=True)
    content = Column(String(20))
    name = Column(String(20))
    time = Column(String(20))
    is_delete = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')  #'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

print("这是一个留言板！")

def menu():
    print("请输入编号来进行操作：")
    print("1.进行留言")
    print("2.删除留言")
    print("3.更新留言")
    print("4.查询所有留言")
    print("0.退出留言板")

def choic(x):
    # 创建session对象:

    if x == 1:
        session = DBSession()
        Content = input("请输入要留言的内容：")
        Name = input("请输入留言人：")
        Time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        is_delete = 0

        # 创建新User对象:
        new_user = User(ID='0',content=Content,name=Name,time=Time,is_delete='0')
        # 添加到session:
        session.add(new_user)
        # 提交即保存到数据库:
        session.commit()
        # 关闭session:
        session.close()
        print("添加成功！")


    if x == 2:
        id = int(input("请输入留言编号："))
        session = DBSession()
        user_willdel = session.query(User).filter_by(ID=id).first()
        user_willdel.is_delete = 1
        session.commit()
        session.close()
        print("删除成功！")


    if x == 3:
        id = int(input("请输入留言编号："))
        Content = input("请输入要留言的内容：")
        Name = input("请输入留言人：")
        Time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        session = DBSession()
        user_result = session.query(User).filter_by(ID=id).first()
        user_result.content = Content
        user_result.name = Name
        user_result.time = Time
        session.commit()
        session.close()
        print("更新成功！")

    if x == 4:
        # 创建session
        session = DBSession()
        # 利用session创建查询，query(对象类).filter(条件).one()/all()
        user = session.query(User).filter().all()
        for x in user:
            print('ID:',x.ID,'content:',x.content,'name:',x.name,'time:',x.time,'is_delete:',x.is_delete)
        # 关闭session
        session.close()
        print("查询成功！")


if __name__ == '__main__':
    menu()
    menu_choic = int(input("请输入0-4任意整数："))
    while(menu_choic):
        choic(menu_choic)
        menu_choic = int(input("请输入0-4任意整数："))
    else:
        print("退出留言板！")