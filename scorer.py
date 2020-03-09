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

all_tags = set(tags_key)
tag_dict = dict(zip(all_tags, range(len(all_tags))))

confusion_matrix = [[0] * len(all_tags) for _ in range(len(all_tags))]

most_tag = ''
most_count = 0
total_correct = 0
for i in range(len(tags_key)):
    actual_tag = tags_key[i]
    predicted_tag = tags_test[i]

    confusion_matrix[tag_dict[actual_tag]][tag_dict[predicted_tag]] += 1

    if actual_tag == predicted_tag:
        if confusion_matrix[tag_dict[actual_tag]][tag_dict[predicted_tag]] > \
                most_count:
            most_tag = actual_tag
            most_count = confusion_matrix[tag_dict[actual_tag]][tag_dict[
                predicted_tag]]

        total_correct += 1

baseline_accuracy = round(most_count / len(tags_key), 2)
accuracy = round(total_correct / len(tags_key), 2)

print("Baseline Accuracy:", baseline_accuracy)
print("Overall Accuracy:", accuracy)

ordered_tags = [''] * len(all_tags)
for tag, num in tag_dict.items():
    ordered_tags[num] = tag

for i in range(len(ordered_tags)):
    if i == 0:
        print("\n     ", end='')
    print(format(ordered_tags[i], '>4'), end=' ')

for i in range(len(all_tags)):
    print("\n", format(ordered_tags[i], '4'), end='')
    for j in range(len(all_tags)):
        print(format(confusion_matrix[i][j], '4'), end=' ')
