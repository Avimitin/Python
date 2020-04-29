# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/4/27 17:14
from urllib import request
import json


# 利用urllib读取JSON，然后将JSON解析为Python对象
def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read()
        json.loads(data)
        return data
