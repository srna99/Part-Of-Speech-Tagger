"""
Serena Cheng
CMSC 416 - PA 3: POS Tagger (tagger.py)
3/8/2020
~~~~~
Problem:
This program addresses the goal of tagging part-of-speech for inputted words
using the bi-gram model and Markov assumption on a modified HMM trained on a
set of tagged data.
Usage:
The user should include the template below when executing:
    (tagged training data) (untagged test data) > (test with tags stdout)
Ex. python3 tagger.py pos-train.txt pos-test.txt > test-with-tags.txt
    > No/DT ,/, [ it/PRP ] [ was/VBD n't/RB Black/NNP Monday/NNP ] ./. etc.
Algorithm:
A greedy tagger is implemented which is based on the probability of a tag
given the word, multiplied by the probability of a tag given the previous
tag. Then, the tag with highest probability is chosen for a given word.
"""

import sys

train_pos = sys.argv[1]  # training set file
test_pos = sys.argv[2]  # test set file

train_content = []  # training copy
test_content = []  # test copy

word_pos_dict = {}  # frequencies of word with specific tags
pos_pos_dict = {}  # frequencies of tags with specific previous tags
pos_dict = {}  # frequencies of tags

test_with_tags = []  # test set with most likely tags

# tokenize pieces of training set
with open(train_pos, 'r', encoding="utf-8-sig") as file:
    train_content.extend(file.read().split())

prev_pos = '.'  # holds previous tags
for term in train_content:
    # skip brackets
    if term == '[' or term == ']':
        continue

    # separate words from tags
    parts = term.rsplit('/', 1)

    word = parts[0]
    pos = parts[1].split('|')[0]

    # add and update frequency count of words with tags
    if word in word_pos_dict.keys():
        if pos in word_pos_dict[word]:
            word_pos_dict[word][pos] += 1
        else:
            word_pos_dict[word][pos] = 1
    else:
        word_pos_dict[word] = {pos: 1}

    # add and update frequency count of tags
    if pos in pos_dict:
        pos_dict[pos] += 1
    else:
        pos_dict[pos] = 1

    # add and update frequency count of tags following previous tags
    if prev_pos in pos_pos_dict.keys():
        if pos in pos_pos_dict[prev_pos]:
            pos_pos_dict[prev_pos][pos] += 1
        else:
            pos_pos_dict[prev_pos][pos] = 1
    else:
        pos_pos_dict[prev_pos] = {pos: 1}

    # update previous tag with current tag
    prev_pos = pos

# tokenize pieces of test set
with open(test_pos, 'r', encoding="utf-8-sig") as file:
    test_content.extend(file.read().split())

prev_pos = '.'
for word in test_content:
    # add unaltered brackets to final set
    if word == '[' or word == ']':
        test_with_tags.append(word)
        continue

    max_tag = "NN"  # most likely tag with default "NN" for unknown words
    max_prob = 0  # highest probability seen for tags

    if word in word_pos_dict.keys():
        # going through every tag seen with word
        for pos in word_pos_dict[word].keys():
            # P(tag_i|word_i) = freq(word_i, tag_i)/freq(tag_i)
            prob_word_pos = word_pos_dict[word][pos] / pos_dict[pos]

            # calculate prob if seen in training set or set to 0
            if pos in pos_pos_dict[prev_pos].keys():
                # P(tag_i|tag_i-1) = freq(tag_i-1, tag_i)/freq(tag_i-1)
                prob_pos_pos = pos_pos_dict[prev_pos][pos] / pos_dict[prev_pos]
            else:
                prob_pos_pos = 0

            # P = P(tag_i|word_i) * P(tag_i|tag_i-1)
            probability = round(prob_word_pos * prob_pos_pos, 6)

            # check and update if there is a higher probability
            if probability > max_prob:
                max_prob = probability
                max_tag = pos

            # update previous tag with current tag
            prev_pos = pos

    # append tag to word and add to final set
    word += ('/' + max_tag)
    test_with_tags.append(word)

# print final set
print(" ".join(test_with_tags))
