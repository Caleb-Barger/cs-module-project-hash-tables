def no_dups(s):
    # given a bunch of strings
    # if a word comes right after the given word 
    # remove it 

    # 1) build a list of all the words first...
    if s != "":

        # sent = s.split()

        sentence = s.split()
        duplicate_word_indxs = []

        for i in range(len(sentence) - 1):
            if sentence[i] == sentence[i + 1]:
                duplicate_word_indxs.append(i + 1) # append the location of the dup!!

        if len(duplicate_word_indxs) > 0:
            # return duplicate_word_indxs
            for i in duplicate_word_indxs:
                sentence[i] = ""
            
            new_sentence = [w for w in sentence if w != ""]

            r = ""
            for w in new_sentence:
                r += w + " "

            return r
            
    
    return s


        
if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
