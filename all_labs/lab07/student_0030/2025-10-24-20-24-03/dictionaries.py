# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    words_counted = {}
    for word in words:
        if word in words_counted:
            words_counted[word] += 1
        else:
            words_counted[word] = 1
    return words_counted

def average_prices(prices):
    counts = {}
    totals = {}
    for item, price in prices:
        if item in totals: 
            totals[item] += price
            counts[item] += 1 
    averages = {}
    for item in totals: 
        avg = totals[item] / counts[item],
        averages[item] = round(avg, 1)
    return averages

def count_bigrams(words):
    bigrams = {}
    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        if pair in bigrams:
            bigrams[pair] += 1
        else:
            bigrams[pair] = 1
    return bigrams
