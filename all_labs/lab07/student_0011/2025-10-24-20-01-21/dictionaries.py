# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    some_dict = {}
    for word in words:
        some_dict[word]=words.count(word)
    return some_dict
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

