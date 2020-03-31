from Test1_2 import dict_test
import json
dic = {}

def write_dic(dic_name):
    with open('test.json','a+') as file:
        dic_json = json.dumps(dic_name)
        file.write(dic_json)


def read_dic():
    with open("test.json", mode="r+") as file:
        dic_json = json.loads(file.read())
        return dic_json


def show_dic():
    name = input("请输入想要展示的键值:")
    print(dic[name])


num = int(input("输入1写入，2读取："))
if num == 1:
    write_dic(dict_test)
else:
    dic = read_dic()
    print(str(dic))
    show_dic()
