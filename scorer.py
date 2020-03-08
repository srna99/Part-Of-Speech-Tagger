"""
Serena Cheng
CMSC 416 - PA 3: POS Tagger (scorer.py)
3/8/2020
~~~~~
Problem:

Usage:

Ex.

Algorithm:

"""

import sys

test_with_tags = sys.argv[1]
test_key = sys.argv[2]

test_tagged_content = []
test_key_content = []

tags_test = []
tags_key = []

all_tags = set()
confusion_matrix = {}

baseline_accuracy = 0
accuracy = 0


def separate_tags(array, sep_array):
    for term in array:
        # skip brackets
        if term == '[' or term == ']':
            continue

        # separate words from tags
        parts = term.rsplit('/', 1)
        pos = parts[1].split('|')[0]
        sep_array.append(pos)


with open(test_with_tags, 'r', encoding="utf-8-sig") as file:
    test_tagged_content.extend(file.read().split())

with open(test_key, 'r', encoding="utf-8-sig") as file:
    test_key_content.extend(file.read().split())

separate_tags(test_tagged_content, tags_test)
separate_tags(test_key_content, tags_key)

all_tags.update(set(tags_key))

for tag1 in all_tags:
    for tag2 in all_tags:
        if tag1 in confusion_matrix.keys():
            confusion_matrix[tag1][tag2] = 0
        else:
            confusion_matrix[tag1] = {tag2: 0}

most_tag = ''
most_count = 0
for i in range(len(tags_key)):
    actual_tag = tags_key[i]
    predicted_tag = tags_test[i]

    confusion_matrix[actual_tag][predicted_tag] += 1

    if confusion_matrix[actual_tag][predicted_tag] > most_count and \
            actual_tag == predicted_tag:
        most_tag = actual_tag
        most_count = confusion_matrix[actual_tag][predicted_tag]

# correct_count = 0
# for ind, term in enumerate(test_key_content):
#     if term == test_tagged_content[ind] or term == '[' or term == ']':
#         correct_count += 1
#
# accuracy = correct_count / len(test_key_content)
# print(accuracy)
