# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def count_words(tup: tuple):
    some_dict = {}
    for ch in tup:
        if ch in some_dict:
            some_dict[ch] += 1
        else:
            some_dict[ch] = 1
    return some_dict
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')

def average_prices(tup:tuple):
    x1=len(tup)
    dic_1={}
    for ch in tup:
        for x in ch:
            if not str ==type(x):
                for y in ch:
                    dic_1[x]=y
    return dic_1
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))


def count_bigrams(tup: tuple):
    some_dict = {}
    for i in range(len(tup) - 1):
        bigram = (tup[i], tup[i + 1])
        if bigram in some_dict:
            some_dict[bigram] += 1
        else:
            some_dict[bigram] = 1
    return some_dict
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))
