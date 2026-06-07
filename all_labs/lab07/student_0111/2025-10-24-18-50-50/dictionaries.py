# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tup):
    some_dict={}
    for i in tup:
        if i not in some_dict:
            some_dict[i]=1
        else:
            some_dict[i]+=1
    return some_dict


def average_prices(prices):
    totals = {}
    counts = {}
    for item, price in prices:
        totals[item] = totals.get(item, 0) + price
        counts[item] = counts.get(item, 0) + 1
    averages = {item: round(totals[item] / counts[item], 2) for item in totals}
    return averages


def count_bigrams(words):
    bigram_counts = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram]+=1
        else:
            bigram_counts[bigram]=1
    return bigram_counts