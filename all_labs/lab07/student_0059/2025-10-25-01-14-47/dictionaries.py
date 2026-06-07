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


def count_bigrams(x = {}):
    some_dict = {}
    for t in range(0, len(x) - 1):
        bigram = (x[t], x[t+1])
        if bigram not in some_dict:
            some_dict[bigram] = 1
        else:
            some_dict[bigram] += 1
    return some_dict
print(count_bigrams())
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

