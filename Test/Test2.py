# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/3/23 13:18
# 带#的注释皆为本章使用知识点
# 无限循环
var = 1
while var == 1:
    # 斐波那契
    x, y = 0, 1
    z = int(input('请输入一个整数值：'))  # 键盘输入
    print('\n')
    if z <= 1:  # if判断
        print('数值过小')
    elif z > 10000:
        print('数值过大')
    else:
        while y < z:  # 语句循环
            print(y, end=',')
            x, y = y, x + y
    print('\n-------------------分割线--------------------')
    # 累加
    Sum = 0
    count = 1
    total = int(input('输入累加的次数:'))
    while count < total:
        Sum = Sum + count
        count += 1
    print('1进行%d次的累加之后值为%d' % (total, Sum))  # 格式化输出
    print('\n-------------------分割线--------------------')
    # for遍历
    str1 = input('请输入一个任意字母:')
    try:
        str2 = int(input('请输入一个任意数字:'))
    except ValueError:
        print('请输入数字！请按下回车重启程序！\n')
        input()
        continue
# 输入类型判断
# input() 默认输入String类型
#    if type(str2) != int:
#        print('请输入正确数字！程序关闭！')
#        exit()
#    else:
#        print()
    str3 = str(input('请再次输入一个任意值:'))
    Set = {str1, str2, str3}
    for st in Set:
        print(st, end='.')
    for num in range(str2):
        print(num)
    # 结束循环
    var = int(input('\n是否要结束程序？输入1继续，输入0结束:'))
else:
    print('程序结束')
