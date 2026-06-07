# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(words):
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

def average_prices(prices):
    total_prices = {}
    total_counts = {}
    for item, price in prices:
        total_prices[item] = total_prices.get(item, 0) + price
        total_counts[item] = total_counts.get(item, 0) + 1

    averages = {}
    for i in total_prices:
        averages[i] = round(total_prices[i] / total_counts[i], 1)
    return averages

def count_bigrams(words):
    bigram_counts = {}
    for i in range(len(words) - 1):
        b = (words[i], words[i+1])
        bigram_counts[b] = bigram_counts.get(b, 0) + 1
    return bigram_counts
