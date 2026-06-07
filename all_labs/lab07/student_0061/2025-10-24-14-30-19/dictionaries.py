# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words_tuple):
    word_counts = {}
    for word in words_tuple:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
def average_prices(commodities):
    total_prices = {}
    counts = {}

    for name, price in commodities:
        if name in total_prices:
            total_prices[name] += price
            counts[name] += 1
        else:
            total_prices[name] = price
            counts[name] = 1
    averages = {}
    for name in total_prices:
        averages[name] = total_prices[name] / counts[name]
    return averages
def count_bigrams(words_tuple):
    bigram_counts = {}
    for i in range(len(words_tuple) - 1):
        bigram = (words_tuple[i], words_tuple[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts