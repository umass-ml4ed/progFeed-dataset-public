# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(words):
    word_counts = {}
    for w in words:
        if w in word_counts:
            word_counts[w] += 1
        else:
            word_counts[w] = 1
    return word_counts


def average_prices(prices):
    totals = {}
    counts = {}
    for item, price in prices:
        totals[item] = totals.get(item, 0) + price
        counts[item] = counts.get(item, 0) + 1
    return {item: totals[item] / counts[item] for item in totals}


def count_bigrams(words):
    bigram_counts = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts

