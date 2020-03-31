# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/3/31 13:33
# json写入
import json
dic_test = {'default':'123','name':'321'}
print(str(dic_test))
dic_json = json.dumps(dic_test)
print(dic_json)
with open('test.json','a+') as file:
    file.write(dic_json)