# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/5/10 9:48

test_dict = {
    range(0, -100, -1): 'freeze',
    range(0, 10): 'COLD',
    range(11, 20): 'calm',
    range(21, 30): 'warm',
    range(31, 40): 'hot'
}

num = 100
key_list = list(test_dict.keys())

for x in range(len(key_list)):
    if num in key_list[x]:
        key = key_list[x]
        print(test_dict[key])

# 比如现在有这么一串每月收入数据
month = [100, 50, 60, 80, 200, 90]
# 我只想要最后一个月和前面几个月的平均值
# 可以用*变量名来融入更多数据，与函数的参数相同
*before, last = month
avg_before = sum(before) / len(before)
print('前几月平均收入：{}，这个月的收入：{}'.format(avg_before, last))
