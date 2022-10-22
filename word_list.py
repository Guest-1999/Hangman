# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:18:21 2022

@author: rahma
"""
import json
filename = 'words_dictionary.json'
with open(filename) as f:
    words = json.load(f)
# print(words)


word_list = []

for word in words.keys():
    word_list.append(word)
    if len(word) <= 3:
        word_list.remove(word)
        
