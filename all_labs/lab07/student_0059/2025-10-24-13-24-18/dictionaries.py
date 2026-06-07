# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(x):
    some_dict = {}
    for i in x:
        if i not in some_dict:
            some_dict[i] = 1
        else:
            some_dict[i] += 1
    return some_dict

print(count_words(x = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')))