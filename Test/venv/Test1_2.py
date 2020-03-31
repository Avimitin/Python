# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/3/29 11:12
print("正在生成字典")
dict_test = {}


def dict_add():
    key = input("请输入一个键值：")
    name = input("请输入键值指向的元素：")
    dict_test[key] = name
    print(dict_test[key])


def dict_delete():
    print(str(dict_test))
    del_name = input("请输入你想要的删除的元素的键值：")
    del dict_test[del_name]


num = 1
while num == 1:
    print('请输入您想要做的事：')
    try:
        num2 = int(input("输入0往字典增加一个新的值，输入1从字典中删除一个值,输入2什么都不做:"))
    except ValueError:
        print("请输入合法数字！")
        continue
    if num2 == 0:
        dict_add()
    elif num2 == 1:
        dict_delete()
    elif num2 == 2:
        pass
    else:
        print("数值错误！请输入正确指令")
        continue
    num = int(input("是否要结束程序？输入0结束，输入1继续："))
