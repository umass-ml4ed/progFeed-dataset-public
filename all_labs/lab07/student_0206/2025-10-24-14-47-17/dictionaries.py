# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def average_prices(comm):
    counts = {}
    totals = {}
    for entry in comm:
        index, price = entry
        counts[index] = counts.get(index, 0) + 1
        totals[index] = totals.get(index, 0.0) + price
    avg_price = {}
    for index in totals:
        avg_price[index] = totals[index] / counts[index]
    return avg_price

def count_bigrams(words):
    bigram_dict = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i+1])
        bigram_dict[bigram] = bigram_dict.get(bigram, 0) + 1
    return bigram_dict
