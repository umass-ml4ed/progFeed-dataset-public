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
    total_prices = {}
    counts = {}
    for commodity, price in prices:
        if commodity in total_prices:
            total_prices[commodity] += price
            counts[commodity] += 1
        else:
            total_prices[commodity] = price
            counts[commodity] = 1
    averages = {}
    for commodity in total_prices:
        averages[commodity] = total_prices[commodity] / counts[commodity]
    return averages

def count_bigrams(words):
    bigram_counts = {}
    if len(words) < 2:
        return bigram_counts
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1]) 
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts