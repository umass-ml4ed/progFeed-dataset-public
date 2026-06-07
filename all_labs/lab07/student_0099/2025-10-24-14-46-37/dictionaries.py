# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def count_words(words):
    counts = {}
    for w in words:
        if w not in counts:
            counts[w] = 1
        else:
            counts[w] += 1
    return counts


def average_prices(data):
    total_price = {}
    count = {}

    for item, price in data:
        if item not in total_price:
            total_price[item] = price
            count[item] = 1
        else:
            total_price[item] += price
            count[item] += 1

    averages = {}
    for item in total_price:
        averages[item] = total_price[item] / count[item]

    return averages


def count_bigrams(words):
    bigram_counts = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram not in bigram_counts:
            bigram_counts[bigram] = 1
        else:
            bigram_counts[bigram] += 1
    return bigram_counts


