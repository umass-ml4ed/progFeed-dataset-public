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
    counts_dict = {}
    totals_dict = {}
    for item, price in prices:
        if item in totals_dict:
            totals_dict[item] += price
            counts_dict[item] += 1
        else:
            totals_dict[item] = price
            counts_dict[item] = 1
    averages = {}
    for item in totals_dict:
        avg = totals_dict[item] / counts_dict[item]
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
