# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(a):
    word_counts = {}
    for w in a:
        if w in word_counts:
            word_counts[w] += 1
        else:
            word_counts[w] = 1
    return word_counts


def average_prices(b):
    totals = {}
    counts = {}
    for name, price in b:
        if name in totals:
            totals[name] += price
            counts[name] += 1
        else:
            totals[name] = price
            counts[name] = 1
    return {name: totals[name] / counts[name] for name in totals}


def count_bigrams(c):
    bigram_counts = {}
    for i in range(len(c) - 1):
        pair = (c[i], c[i + 1])
        if pair in bigram_counts:
            bigram_counts[pair] += 1
        else:
            bigram_counts[pair] = 1
    return bigram_counts