# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(t):
    d = {}
    for word in t:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d


def average_prices(s):
    d = {}
    n = {}
    averages = {}
    for item, price in s:
            if item not in d:
                d[item] = price
                n[item] = 1
            else:
                d[item] += price
                n[item] += 1
    for item in d:
        averages[item] = d[item] / n[item] 
    return averages


def count_bigrams(f):
    d = {}
    previous = None
    for i in f:
        if previous is not None: 
            bigram = (previous, i)   
            if bigram not in d:
                d[bigram] = 1
            else:
                d[bigram] += 1
        previous = i
    return d
