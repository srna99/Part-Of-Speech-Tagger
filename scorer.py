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

tagged_test_content = []
key_content = []

baseline_accuracy = 0
accuracy = 0

with open(test_with_tags, 'r', encoding="utf-8-sig") as file:
    tagged_test_content.extend(file.read().split())

with open(test_key, 'r', encoding="utf-8-sig") as file:
    key_content.extend(file.read().split())

correct_count = 0
for ind, term in enumerate(key_content):
    if term == tagged_test_content[ind] or term == '[' or term == ']':
        correct_count += 1

accuracy = correct_count / len(key_content)
print(accuracy)




