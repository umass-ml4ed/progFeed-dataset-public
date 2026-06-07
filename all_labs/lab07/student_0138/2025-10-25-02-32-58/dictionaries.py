# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(tuple_of_words):
    some_dict = {}
    for s in tuple_of_words:
        if s not in some_dict:#
            some_dict[s] = 1
        else:
            some_dict[s] += 1
    return some_dict

# words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
# print(count_words(words))

def average_prices(prices):
    total = {}
    count = {}
    for names, p in prices:
        if names in total:
            total[names] += p
            count[names] += 1
        else:
            total[names] = p
            count[names] = 1
    average = {}
    for names in total:
        average[names] = total[names] / count[names]
    return average

# prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
# print(average_prices(prices))

def count_bigrams(words):
    bigrams = {}
    for b in range(len(words) - 1):
        pairs = (words[b], words[b+1])
        if pairs not in bigrams:
            bigrams[pairs] = 1
        else:
            bigrams[pairs] += 1
    return bigrams

# words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
# print(count_bigrams(words))