# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    some_dict = {}
    for s in words:
        if s in some_dict:
            some_dict[s] += 1
        else:
            some_dict[s] = 1
    return some_dict

def average_prices(prices):
    total_price = {}
    total_num = {}
    for item, price in prices:
        if item in total_price:
            total_price[item] += price
            total_num[item] += 1
        else:
            total_price[item] = price
            total_num[item] = 1
    
    avgs = {}
    for item in total_price:
        avgs[item] = total_price[item] / total_num[item]
    return avgs
        

def count_bigrams(words):
    some_dict = {}
    
    if len(words) < 2:
        return some_dict

    for i in range(len(words) -1):
        bigram = (words[i], words[i+1])
        if bigram in some_dict:
            some_dict[bigram] += 1
        else:
            some_dict[bigram] = 1
    return some_dict
