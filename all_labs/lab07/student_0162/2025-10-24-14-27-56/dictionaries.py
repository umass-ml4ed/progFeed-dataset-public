# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tup : tuple):
    word_dict = {}

    for i in tup:
        if i not in word_dict:
            word_dict[i] = 1
        else:
            word_dict[i] += 1
    return word_dict

