# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/3/31 13:33
# json写入
import json
dic_test = {'default': '123', 'name': '321'}
print(str(dic_test))
dic_json = json.dumps(dic_test)
print(dic_json)
with open('test.json', 'w+') as file:
    file.write(dic_json)

dic2 = {'key': 'value', 'yyqgg': 'YYQGG', 'inm': ['114514', '1919810', '24']}
print(json.dumps(dic2, sort_keys=True, indent=4))
print('key:{0[key]:s},YYQGG:{0[yyqgg]:s},name:{1[name]:s}'.format(dic2,dic_test))

