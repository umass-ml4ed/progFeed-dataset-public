# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    numberwords = {}
    for x in words:
        if x in numberwords:
            numberwords[x] += 1
        else:
            numberwords[x] = 1
    return numberwords

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
    averages = {item: totals[item] / counts[item] for item in totals}
    return averages

def count_bigrams(words):
    bigram_counts = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts