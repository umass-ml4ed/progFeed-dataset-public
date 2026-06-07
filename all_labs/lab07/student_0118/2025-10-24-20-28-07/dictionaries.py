# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(words):
    d = {}
   
    for w in words:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1
    return d

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))


def average_prices(prices):
    d_t = {}
    d_n = {}
    for item, price in prices:
        if item in d_t:
            d_t[item] += price
            d_n[item] += 1
        else:
            d_t[item] = price
            d_n[item] = 1
    return {item: d_t[item] / d_n[item] for item in d_t}

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(s):
    bigram_counts = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

