# most frequent (ordered)
frequent_ordering = [
            'E', 'T', 'A', 'O', 'H', 
            'N', 'R', 'I', 'S', 'D', 
            'L', 'W', 'U', 'G', 'F',
            'B', 'M', 'Y', 'C', 'P', 
            'K', 'V', 'Q', 'J', 'X', 
            'Z'
]

char_count = {}

# read in the file
with open('ciphertext.txt', 'r') as f:
    data = f.read()
# iterate over the info
for c in data:
    if c in frequent_ordering: # <--- using this as valid characters for right now

        if c not in char_count:
            char_count[c] = 0
        
        # counting occurences of each letter (ignoring nonletters)
        char_count[c] += 1

# after building a hash map of all the characters with their counts
# - map characters values to the keys given ^^

encode_key = {}

# get the items as a list from the char_count map
char_count_arr = list(char_count.items())
char_count_arr.sort(key=lambda e: e[1], reverse=True)

# print(char_count_arr)
j = 0
for i in char_count_arr:
   encode_key[i[0]] = frequent_ordering[j]
   j += 1    

# after building the new hash map (should be what was used to encode the text)
# iterate through the data and build a return string based off of the key

r = ""
for c in data:
    if c in frequent_ordering:
        # compare with key
        c = encode_key[c]
    r += c

print(r)
