# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/3/25 15:31
# 函数练习


def hello(name):
    # 一个简单的函数
    print("Hello " + name)


hello("and fuck you")

# 循环计算矩形面积
var = 1
while var == 1:
    def square(w, l):
        """一个简单的计算面积的程序 """
        return w * l


    try:
        width = int(input("请输入宽度:"))
        length = int(input("请输入长度:"))
    except ValueError:
        print("请输入数字")
        continue
    print("长为%d宽为%d的矩形面积为：%d" % (width, length, square(width, length)))
    var = int(input("是否要终止程序，终止请按0，继续请按1"))

# Python只引用对象，赋值本身属于将变量指向对象
a = 2  # 将a变量指向int 2对象
a = 3  # 将a变量指向int 3对象


# a本身是没有任何类型的


def change_num(b):
    b = 10
    return b


print(change_num(a))  # a = 10(将a指向了10）
change_num(a)
print(a)  # a = 3 （a本身不改变，还是指向3）


# 默认值和传参
def telephone_book(name, phone="123", num=1):
    """默认值要放在最后面，顺序可以无所谓"""
    print("第%d的用户名为%s，电话号码是%s" % (num, name, phone))


num2 = int(input("请输入编号"))
name2 = str(input("请输入名字;"))
phone2 = str(input("请输入电话"))
telephone_book(name=name2, )
telephone_book(num=num2, name=name2, phone=phone2)  # 做好标识符可以打乱顺序


def test(aa, b, vd, *var):
    """*号后传入的数据指向元组类
    所以如果想加多余值不可以直接sum = aa + b + vd + var
    需要使用循环语句将元组内数字传出"""
    print(aa + b + vd)
    print(var)
    count = len(var)
    num = 0
    while count != 0:
        num += var[count-1]
        count -= 1
    sum = aa + b + vd + num
    return sum


print(test(10, 20, 30, 40, 50, 60, 70))


print(test(1, 2, 3))
# lambda是简单版本def，没有代码块，用法：lambda arg1, arg2: 函数表达式
test2 = lambda aa, b, vd: aa + b + vd
print("lambda是用来写简单函数的def")
print(test2(1, 2, 3))


def product(x, *y):
    if y == ():
        return x
    else:
        pro_sum = x
        for unit in y:
            pro_sum = pro_sum*unit
        return pro_sum
