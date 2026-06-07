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

def average_prices(items):
    total_prices = {} 
    total_counts = {} 
    for name, price in items:
        if name in total_prices:
            total_prices[name] += price
            total_counts[name] += 1
        else:
            total_prices[name] = price
            total_counts[name] = 1
    averages = {}
    for name in total_prices:
        averages[name] = total_prices[name] / total_counts[name]
    return averages

def count_bigrams(words):
    bigram_counts = {}
    if len(words) < 2:
        return {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts