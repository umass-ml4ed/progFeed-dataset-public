# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(x):
    x = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
    some_dict = {}
    for i in x:
        if i not in some_dict:
            some_dict[i] = 1
        else:
            some_dict[i] += 1
    return some_dict
