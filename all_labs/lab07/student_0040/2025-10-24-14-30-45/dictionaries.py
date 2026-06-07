# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(words):
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def average_prices(prices):
    total_price = {}
    count = {}

    for item, price in prices:
        if item in total_price:
            total_price[item] += price
            count[item] += 1
        else:
            total_price[item] = price
            count[item] = 1

    averages = {}
    for item in total_price:
        averages[item] = round(total_price[item] / count[item], 1)

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
