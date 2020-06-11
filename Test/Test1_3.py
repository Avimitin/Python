# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/4/22 15:36
import re
# 输出平方列表
square = []
for x in range(5):
    square.append(x**2)
print(square)

square2 = [x**3 for x in range(5)]
print(square2)

list1 = [(x, y)for x in square for y in square2 if x != y]
print(list1)

list2 = [x for x in square2 if x % 2 == 0]
print(list2)

list3 = ['apple', 'abandon', 'apart']


def change_a(word):
    new_word = re.sub(r'a', '呐', word)
    return new_word


list4 = [change_a(word) for word in list3]
print(list4)

for x, y in zip(list3, list4):
    print('before:{0}, after:{1}'.format(x, y))
