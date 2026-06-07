# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    return word_counts
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(prices):
    total_prices = {}
    counts = {}
    for commodity, price in prices:
        if commodity not in total_prices:
            total_prices[commodity] = price
            counts[commodity] = 1
        else:
            total_prices[commodity] += price
            counts[commodity] += 1
    averages = {}
    for commodity in total_prices:
        averages[commodity] = total_prices[commodity] / counts[commodity]
    return averages    
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(words):
    bigram_counts = {}
    if len(words) < 2:
        return bigram_counts
    for i in range(len(words) - 1):
        bigram = (words[i], words[i+1])
        if bigram not in bigram_counts:
            bigram_counts[bigram] = 1
        else:
            bigram_counts[bigram] += 1
    return bigram_counts
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))