# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

some_dict = {}

def count_words(tup):
    for word in tup:
        if word in some_dict:
            some_dict[word] += 1
        else:
            some_dict[word] = 1
    return some_dict


def average_prices(tup):
    price_dict = {}
    count_dict = {}
    for item, price in tup:
        if item in price_dict:
            price_dict[item] += price
            count_dict[item] += 1
        else:
            price_dict[item] = price
            count_dict[item] = 1
    for item in price_dict:
        price_dict[item] /= count_dict[item]
    return price_dict


some_dict2 = {}

def count_bigrams(tup):
    for i in range(len(tup) - 1):
        bigram = (tup[i], tup[i + 1])
        if bigram in some_dict2:
            some_dict2[bigram] += 1
        else:
            some_dict2[bigram] = 1
    return some_dict2

