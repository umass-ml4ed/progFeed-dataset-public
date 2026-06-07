# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    result = {}
    for w in words:
        if w in result:
            result[w] = result[w] + 1
        else:
            result[w] = 1
    return result


def average_prices(prices):
    totals = {}
    counts = {}
    for name, price in prices:
        if name in totals:
            totals[name] = totals[name] + price
            counts[name] = counts[name] + 1
        else:
            totals[name] = price
            counts[name] = 1
    return {name: totals[name] / counts[name] for name in totals}


def count_bigrams(words):
    result = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in result:
            result[bigram] = result[bigram] + 1
        else:
            result[bigram] = 1
    return result
