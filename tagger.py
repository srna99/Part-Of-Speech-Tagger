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

import sys

train_pos = sys.argv[1]
test_pos = sys.argv[2]

train_content = []
test_content = []

word_pos_dict = {}
pos_pos_dict = {}
pos_dict = {}

test_with_tags = []

with open(train_pos, 'r', encoding="utf-8-sig") as file:
    train_content.extend(file.read().split())

prev_pos = '.'
for term in train_content:
    if term == '[' or term == ']':
        continue

    parts = term.rsplit('/', 1)

    word = parts[0]
    pos = parts[1].split('|')[0]

    if word in word_pos_dict.keys():
        if pos in word_pos_dict[word]:
            word_pos_dict[word][pos] += 1
        else:
            word_pos_dict[word][pos] = 1
    else:
        word_pos_dict[word] = {pos: 1}

    if pos in pos_dict:
        pos_dict[pos] += 1
    else:
        pos_dict[pos] = 1

    if prev_pos in pos_pos_dict.keys():
        if pos in pos_pos_dict[prev_pos]:
            pos_pos_dict[prev_pos][pos] += 1
        else:
            pos_pos_dict[prev_pos][pos] = 1
    else:
        pos_pos_dict[prev_pos] = {pos: 1}

    prev_pos = pos

with open(test_pos, 'r', encoding="utf-8-sig") as file:
    test_content.extend(file.read().split())

prev_pos = '.'
for word in test_content:
    if word == '[' or word == ']':
        test_with_tags.append(word)
        continue

    max_tag = "NN"
    max_prob = 0

    if word in word_pos_dict.keys():
        for pos in word_pos_dict[word].keys():
            prob_word_pos = word_pos_dict[word][pos] / pos_dict[pos]

            if pos in pos_pos_dict[prev_pos].keys():
                prob_pos_pos = pos_pos_dict[prev_pos][pos] / pos_dict[prev_pos]
            else:
                prob_pos_pos = 0

            probability = round(prob_word_pos * prob_pos_pos, 6)

            if probability > max_prob:
                max_prob = probability
                max_tag = pos

            prev_pos = pos

    word += ('/' + max_tag)
    test_with_tags.append(word)

print(" ".join(test_with_tags))
