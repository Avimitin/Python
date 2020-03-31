# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/3/25 11:09
# 迭代器
list1 = [123, 'abc', 456, 'efg']
list2 = [321, 'ABC', 654, 'EFG']
it = iter(list1)

print(next(it))
print(next(it))
for x in it:
    print(x, end=',')
# 迭代器一旦遍历完之后就不可以再迭代
# for x in it:
#   print(x, end=',')
