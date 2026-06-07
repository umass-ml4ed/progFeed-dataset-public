# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    dict = {}
    for i in words:
        if i not in words:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))