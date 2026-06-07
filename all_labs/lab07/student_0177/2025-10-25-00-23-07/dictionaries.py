# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def count_words(words):
    word_counts = {} 
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def average_prices(prices):
    price_sums = {}     
    price_counts = {}   
    for item, price in prices:
        if item in price_sums:
            price_sums[item] += price
            price_counts[item] += 1
        else:
            price_sums[item] = price
            price_counts[item] = 1
    averages = {}
    for item in price_sums:
        averages[item] = round(price_sums[item] / price_counts[item], 1)
    return averages

def count_bigrams(words):
    bigram_counts = {} 
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts
