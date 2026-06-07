# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    word_count = {}
    for w in words:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1
    return word_count


def average_prices(prices):
    total, count = {}, {}
    for item, price in prices:
        total[item] = total.get(item, 0) + price
        count[item] = count.get(item, 0) + 1
    return {item: total[item] / count[item] for item in total}


def count_bigrams(words):
    bigrams = {}
    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        bigrams[pair] = bigrams.get(pair, 0) + 1
    return bigrams
