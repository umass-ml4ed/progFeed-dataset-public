# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    counts = {}

    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1

    return counts


def average_prices(items):
    prices_by_name = {}

    for name, price in items:
        if name in prices_by_name:
            prices_by_name[name].append(price)
        else:
            prices_by_name[name] = [price]

    averages = {}
    for name in prices_by_name:
        prices_list = prices_by_name[name]
        averages[name] = sum(prices_list) / len(prices_list)

    return averages

def count_bigrams(words):
    counts = {}

    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        if pair in counts:
            counts[pair] += 1
        else:
            counts[pair] = 1

    return counts
