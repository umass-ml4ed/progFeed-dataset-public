# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(string):
    some_dict = {}
    for i in string:
        if i in some_dict:
            some_dict[i] += 1
        else:
            some_dict[i] = 1
    return some_dict

def average_prices(com):
    total_price = {}
    total_num = {}
    for x, y in com:
        if x in total_num:
            total_num[x] += 1
            total_price[x] += y
        else:
            total_num[x] = 1
            total_price[x] = y
    avg = {}
    for x in total_price:
        avg[x] = total_price[x] / total_num[x]
    return avg

def count_bigrams(tup):
    some_dict = {}
    for x in range(len(tup)-1):
        bigram = (tup[x], tup[x+1])
        if bigram in some_dict:
            some_dict[bigram] += 1
        else:
            some_dict[bigram] = 1
    return some_dict