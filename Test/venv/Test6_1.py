# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/3/31 16:38
# json读取
import json
dic = {}
with open('test.json','r+') as file:
    dic_json = file.read()
dic = json.loads(dic_json)
print(str(dic))
