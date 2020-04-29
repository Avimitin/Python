# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/4/22 11:59
# 闭包返回函数扩展


def counter():
    x = 0
    print(x, end=',')
    x += 1
    print(x, end=',')

    def count_counter():
        nonlocal x
        x += 1
        print(x, end=',')
        return x

    return count_counter


a = counter()
counter(), counter(), counter()
a(), a(), a()

