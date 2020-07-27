# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/4/26 12:14


def test_input(num, num2, num3):
    if num == 1 or 2:
        """always True"""
        print('True')
    else:
        print('False')

    if num2 == 1 or num2 == 2:
        """This will declare num2 equals to 1|2 or not"""
        print('True')
    else:
        print('False')

    if num3 == (1 or 2):
        """If num3 == 1 will return True, else return 2"""
        print('True')
    else:
        print('False')


test_input(3, 3, 3)
