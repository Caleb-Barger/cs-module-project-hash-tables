import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

words = words.split()

word_structure = {}

# TODO: analyze which words can follow other words
# Your code here
for i in range(len(words) - 3):
    if words[i] not in word_structure:
        word_structure[words[i]] = words[i + 1: i  + random.randint(1, 3) + 1]

# print(word_structure)
for k, v in word_structure.items():
    print(f"WORD - {k} | MAY BE FOLLOWED WITH - {v}\n\n")




# TODO: construct 5 random sentences
# Your code here

