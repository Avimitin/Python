# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/4/1 16:57
import yaml
test_dic = {}
with open('test.yml','r+') as test_file:
    test_dic = yaml.load(test_file,Loader=yaml.FullLoader)
print(str(test_dic))
print(test_dic.keys())
print(list(test_dic.keys())[1])