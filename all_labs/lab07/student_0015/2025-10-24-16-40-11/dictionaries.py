# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED

def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def average_prices(data):
    total_price = {}
    count = {}

    for item, price in data:
        if item in total_price:
            total_price[item] += price
            count[item] += 1
        else:
            total_price[item] = price
            count[item] = 1

    averages = {}
    for item in total_price:
        averages[item] = total_price[item] / count[item]

    return averages


def count_bigrams(words):
    bigram_count = {}

    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_count:
            bigram_count[bigram] += 1
        else:
            bigram_count[bigram] = 1

    return bigram_count


