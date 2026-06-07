# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(tup):
    some_dict = {}
    for i in tup:
        if i in some_dict:
            some_dict[i] += 1
        else:
            some_dict[i] = 1
    return some_dict

def average_prices(tup):
    price_totals = {}
    count_totals = {}
    for name, price in tup:
        if name in price_totals:
            price_totals[name] += price
            count_totals[name] += 1
        else:
            price_totals[name] = price
            count_totals[name] = 1
    return {name: price_totals[name]/ count_totals[name] for name in price_totals}

def count_bigrams(tup):
    bigram_count = {}
    for i in range(len(tup) - 1):
        bigram = (tup[i], tup[i+1])
        if bigram in bigram_count:
            bigram_count[bigram] += 1
        else:
            bigram_count[bigram] = 1
    return bigram_count
