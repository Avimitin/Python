# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/4/26 10:52
import Test11
import re


class NewTest(Test11.Test):
    def __init__(self, name, age, place, gender):
        super().__init__(name, age, place)
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        gen_list = ['male', 'female', 'Female', 'Male', 'MALE', 'FEMALE']
        if gender in gen_list:
            self.__gender = gender
        else:
            raise ValueError('Please input correct gender')


if __name__ == '__main__':
    test = NewTest('test', 24, '下北泽', 'male')
    test.set_gender('Male')
    print('名字势{},今年{}，家住{}，势{}'.format(test.name, test.age, test.place, test.get_gender()))
