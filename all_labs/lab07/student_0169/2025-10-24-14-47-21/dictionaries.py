# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    word_count = {}  
    for w in words:
        if w not in word_count:
            word_count[w] = 1
        else:
            word_count[w] += 1
    return word_count


def average_prices(prices):
    total = {}   
    count = {}   
    for item, price in prices:
        if item not in total:
            total[item] = price
            count[item] = 1
        else:
            total[item] += price
            count[item] += 1
    avg = {}
    for item in total:
        avg[item] = total[item] / count[item]
    return avg

def count_bigrams(words):
    bigrams = {}
    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        if pair not in bigrams:
            bigrams[pair] = 1
        else:
            bigrams[pair] += 1
    return bigrams

