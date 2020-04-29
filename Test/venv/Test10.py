# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/4/21 11:16
# 返回函数和装饰器


# test1
# 设计一个迭代器+
def generator(b):
    while b > 0:
        yield b
        b -= 1
        return b


a = int(input('输入数字'))
"""
while True:
    try:
        next(g)
    except StopIteration:
        print("program done")
        break
"""


# 设计一个返回函数，调用再迭代
def create_counter():
    x = 0

    def counter():
        """
        引用外部函数的变量有两种办法：
        1. 使用可改变的参数属性，比如列表，字典
        2. 在内部函数用 nonlocal 关键字声明非本地空间变量
        """
        nonlocal x
        x += 1
        return x

    return counter


# 定义一个过滤器，过滤输入的函数
def num_filter(x):
    if type(x) == int:
        def returner(func):
            def inner():
                return func(x)
            return inner
        return returner
    elif type(x) == float:
        print("请输入整数！")
        exit()
    else:
        print("非法字符！")
        exit()


y = input("请输入一个整数数值")


@num_filter(y)
def main(num):
    print("正在输出"+str(num)+"次整数")
    counter = create_counter()

    while num > 0:
        a_count = counter()
        print(a_count)
        num -= 1


if __name__ == '__main__':
    main()
