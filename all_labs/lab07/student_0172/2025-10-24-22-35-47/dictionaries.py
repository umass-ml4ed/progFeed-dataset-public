# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    amount = {}
    for word in words:
        if word in amount:
            amount[word] += 1
        else:
            amount[word] = 1
    return amount


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