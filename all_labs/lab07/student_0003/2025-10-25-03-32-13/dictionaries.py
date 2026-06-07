# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    d = {}
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    return d


def average_prices(main_tup):
    d = {}
    for name, price in main_tup:
        if name in d:
            d[name].append(price)
        else:
            d[name] = [price]

    for name in d:
        d[name] = sum(d[name]) / len(d[name])

    return d


def count_bigrams(words):
    d = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i+1])
        if bigram in d:
            d[bigram] += 1
        else:
            d[bigram] = 1
    return d
