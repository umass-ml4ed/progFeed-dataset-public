# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words: tuple):
    some_dict = {}
    for word in words:
        if word not in some_dict:
            some_dict[word] = 1
        else:
            repeats = words.count(word)
            some_dict[word] = repeats
    return some_dict
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))



