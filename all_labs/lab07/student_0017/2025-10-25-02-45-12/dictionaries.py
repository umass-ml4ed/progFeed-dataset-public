# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def count_words(words):
    result = {}
    for w in words:
        if w in result:
            result[w] += 1
        else:
            result[w] = 1
    return result


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

    averages = {}
    for item in totals:
        averages[item] = totals[item] / counts[item]
    return averages


def count_bigrams(words):
    result = {}
    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        if pair in result:
            result[pair] += 1
        else:
            result[pair] = 1
    return result
