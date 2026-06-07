# Your first line of Python code
# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def average_prices(prices):
    totals = {}
    counts = {}
    for name, price in prices:
        totals[name] = totals.get(name, 0) + price
        counts[name] = counts.get(name, 0) + 1
    averages = {}
    for name in totals:
        averages[name] = totals[name] / counts[name]
    return averages

def count_bigrams(words):
    bigram_counts = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i+1])
        bigram_counts[bigram] = bigram_counts.get(bigram, 0) + 1
    return bigram_counts
