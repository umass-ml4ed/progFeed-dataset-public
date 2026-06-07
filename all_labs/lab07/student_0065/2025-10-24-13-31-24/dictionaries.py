# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words: tuple):
    some_dict = {}
    i = 0
    for word in words:
        if word not in some_dict:
            i += 1
            some_dict[word] = i
    return some_dict
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))



