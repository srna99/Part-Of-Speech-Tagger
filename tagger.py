"""
Serena Cheng
CMSC 416 - PA 3: POS Tagger (tagger.py)
3/8/2020
~~~~~
Problem:

Usage:

Ex. 
    
Algorithm:

"""
"""
For training: keep track of how often see word with tag and tags after another tag
(Dict[pos[i]][word[i]] or dict[pos[i]][pos[i+1]])
2 bigram tables (word/tag and tag/tag) and 1 unigram table (total tags)
"""

import sys

train_pos = sys.argv[1]
test_pos = sys.argv[2]

word_pos_dict = {}
pos_pos_dict = {}
pos_dict = {}

train_content = []

with open(train_pos, 'r', encoding="utf-8-sig") as file:
    train_content.extend(file.read().split())

for term in train_content:
    if term == '[' or term == ']':
        continue
    else:
        parts = term.rsplit('/', 1)

        word = parts[0]
        pos = parts[1]

        if word in word_pos_dict.keys():
            if pos in word_pos_dict[word]:
                word_pos_dict[word][pos] += 1
            else:
                word_pos_dict[word][pos] = 1
        else:
            word_pos_dict[word] = {pos: 1}








