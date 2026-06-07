# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def average_prices(comm):
    # comm is an iterable of (key, price) pairs
    counts = {}
    totals = {}
    for entry in comm:
        index, price = entry
        counts[index] = counts.get(index, 0) + 1
        totals[index] = totals.get(index, 0.0) + price

    # compute averages per key
    avg_price = {}
    for index in totals:
        avg_price[index] = totals[index] / counts[index]
    return avg_price

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))