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

def average_prices(prices):
    totals = {}
    counts = {}
    for name, price in prices:
        if name in totals:
            totals[name] += price
            counts[name] += 1
        else:
            totals[name] = price
            counts[name] = 1
    averages = {}
    for name in totals:
        averages[name] = totals[name] / counts[name]
    return averages

def count_bigrams(words):
    d = {}
    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        if pair in d:
            d[pair] += 1
        else:
            d[pair] = 1
    return d
