# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(words):
    counts = {}
    for i in words:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
    return counts

def average_prices(items):
    totals = {}
    amounts = {}

    for name, price in items:
        if name not in totals:
            totals[name] = price
            amounts[name] = 1
        else:
            totals[name] += price
            amounts[name] += 1
    averages = {}
    for name in totals:
        averages[name] = totals[name] / amounts[name]
    return averages

def count_bigrams(words):
    bigrams = {}
    for i in range(len(words) - 1):
        bg = (words[i], words[i + 1])
        if bg not in bigrams:
            bigrams[bg] = 1
        else:
            bigrams[bg] += 1
    return bigrams
