# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/4/24 17:19


class Test:

    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place
        self.racist = 'human'

    def change_racist(self, racist):
        self.racist = racist


if __name__ == '__main__':
    dts = Test('Duetosell', 24, '下北泽')
    dts.occupation = '学生'
    dts.change_racist('inm民')
    print('DTS叫做{0},年龄{1}岁，居于{2}，是{3}'.format(dts.name, dts.age, dts.place, dts.occupation))
