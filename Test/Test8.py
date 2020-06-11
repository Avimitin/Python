# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/4/4 19:23
import re
sentence = '/add keyword=value'
text = sentence[5:]
new_sentence = re.split(r'=', text)
sentence_dic = {new_sentence[0]: new_sentence[1]}
print(str(sentence_dic))
