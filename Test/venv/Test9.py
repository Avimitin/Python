# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/4/13 17:11
# 廖雪峰课后习题
# map()和reduce()的使用
from functools import reduce


# 1. 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def high2low(name):
    return name[0].upper() + name[1:].lower()


result = list(map(high2low, ['Adam', 'LiSA', 'Bart']))
print(result)

print('--------------------------------------------')


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# 解法1
def product(x, y):
    return x*y


def prod(a_list):
    return reduce(product, a_list)


# 解法2
def prod2(a_list):
    return reduce(lambda x, y: x*y, a_list)


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
