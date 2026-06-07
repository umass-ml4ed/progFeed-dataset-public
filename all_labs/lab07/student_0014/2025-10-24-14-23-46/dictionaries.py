# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    dict = {}
    for i in words:
        if i not in words:
            dict[1] = 1
        else:
            dict[1] += 1
    return dict
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))