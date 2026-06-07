# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    count = {}
    for word in words:
        if words in count:
            count[word] += 1
        else:
            count[word] = 1
    return word 

def average_prices(names, prices):
    average_price = {}
    for name in names:
        if name in average_price:
            average_price[name] += 1
        else: 
            average_price[prices] = 1
    return prices
