# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def average_prices(prices):
    totals = {}
    counts = {}
    for item, price in prices:
        if item in totals:
            totals[item] += price
            counts[item] += 1
        else:
            totals[item] = price
            counts[item] = 1
    return {item: totals[item] / counts[item] for item in totals}

def count_bigrams(words):
    bigrams = {}
    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        if pair in bigrams:
            bigrams[pair] += 1
        else:
            bigrams[pair] = 1
    return bigrams
