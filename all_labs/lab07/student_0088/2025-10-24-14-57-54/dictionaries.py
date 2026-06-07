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

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))

def average_prices(prices):
    total_price = {}
    count = {}
    for name,price in prices:
        if name in total_price:
            total_price[name] += price
            count[name] += 1
        else:
            total_price[name] = price
            count[name] = 1
    average = {}
    for name in total_price:
        average[name] = total_price[name] / count[name]
    return average

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')

def count_bigrams(words):
    bigram_counts = {}
    for i in range(len(words) - 1):
        bigram = (words[i],words[i+1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts