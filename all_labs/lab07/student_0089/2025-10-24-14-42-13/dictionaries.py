# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(str):
    some_dict = {}
    for i in str:
        if i not in some_dict:
            some_dict[i] = 1
        elif i in some_dict:
            some_dict[i] += 1
    return some_dict

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))
