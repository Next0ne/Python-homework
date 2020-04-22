# -*- encoding: utf-8 -*-
'''
@File : fight.py
@Time : 2020/04/17 11:19:08
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

from dog import dog
from person import person
import random 


def fight(flag):   ##全体狗攻击人一次  或者  全体人攻击狗一次
    global start
    if flag == 0:
        print("狗攻击人!")
        for i in range(0,len(Dog)):
            i = random.randint(0,2)
            if Dog[i].health <= 0 or Dog[i].ATK <= 0:
                continue
            else:
                target = random.choice(Person)
                while target.health <= 0:
                    Person.remove(target)
                    target = random.choice(Person)
                    if not Person:
                        print("所有的人的生命值都不足1")
                        return 0
                else:
                    target.be_attacked(Dog[i])
                    print("狗%d 攻击 人%d，这个人生命值还有 %d，攻击力还有 %d" %(i+1,(Person.index(target))+1,target.health,target.ATK))
                    start = 1
                    return 1
    if flag == 1:
        print("人攻击狗!")
        for i in range(0,len(Person)):
            if Person[i].health <= 0 or Person[i].ATK <= 0:
                continue
            else:
                target = random.choice(Dog)
                while target.health <= 0:
                    Dog.remove(target)
                    target = random.choice(Dog)
                    if not Dog:
                        print("所有的狗的生命值都不足1")
                        return 0
                else:
                    target.be_attacked(Person[i])
                    print("人%d 攻击 狗%d，这个狗生命值还有 %d，攻击力还有 %d" %(i+1,(Dog.index(target))+1,target.health,target.ATK))
                    start = 0
                    return 1

start = random.randint(0,1)
dog1 = dog()
dog2 = dog()
dog3 = dog()
person1 = person()
person2 = person()
Dog = [dog1,dog2,dog3]
Person = [person1,person2]
fight(start)
while fight(start) == 1:
    fight(start)
else:
    print("游戏结束！")
