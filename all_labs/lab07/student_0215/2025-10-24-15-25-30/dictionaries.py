# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(tuple):
    some_dict = {}
    for word in tuple:
        if word in some_dict:
            some_dict[word] += 1
        else:
            some_dict[word] = 1
    return some_dict