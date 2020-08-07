# Your code here

blacklist = [
            ':', ';', ',', '.', '-', '+', '=', 
            '/', '\\', '|', '[', ']', '{', '}', 
            '(', ')', '*', '^', '&', '"'
        ]

with open("robin.txt", 'r') as f:
    data = f.read()

r = ""
for c in data:
    if c not in blacklist:
        r += c

word_count = {}

r = r.split()

for w in r:
    if w not in word_count:
        word_count[w] = 0
    word_count[w] += 1

word_count_list = list(word_count.items())
word_count_list.sort(key=lambda e: e[1], reverse=True)

N_WORDS = 20
c_word = 1

for w in word_count_list:
    print(f"{w[0]} - {'#' * w[1]}")

    # print most used n words
    c_word += 1
    if c_word == N_WORDS:
        break
