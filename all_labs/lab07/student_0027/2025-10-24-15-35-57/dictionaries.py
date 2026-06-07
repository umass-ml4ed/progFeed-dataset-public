# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def average_prices(prices):
    totals = {}
    counts = {}
    for item, price in prices:
        totals[item] = totals.get(item, 0) + price
        counts[item] = counts.get(item, 0) + 1
    return {item: totals[item] / counts[item] for item in totals}


def count_bigrams(words):
    bigram_count = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        bigram_count[bigram] = bigram_count.get(bigram, 0) + 1
    return bigram_count
