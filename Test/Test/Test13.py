# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/4/27 17:14
# 爬虫豆瓣搜索小丑。
import requests
from bs4 import BeautifulSoup

header = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.24 ' \
         'Safari/537.36 Edg/83.0.478.18 '

r = requests.get('https://www.douban.com/search', params={'q': '小丑'}, headers={'User-Agent': header})
soup = BeautifulSoup(r.text, 'html5lib')

if __name__ == '__main__':
    result = soup.find(class_='title')
    name = result.h3.a.string
    tag = result.h3.span.string
    rating = result.find(class_='rating_nums').string
    details = result.find(class_='subject-cast').string
    link = result.h3.a['href']
    print(name, tag, rating, details, link)
