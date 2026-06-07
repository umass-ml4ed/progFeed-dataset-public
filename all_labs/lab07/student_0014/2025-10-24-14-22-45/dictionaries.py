# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    words = {}
    for i in words:
        if i not in words:
            words[1] = 1
        else:
            words[1] += 1
    return words
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))