# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tuple):
    some_dict = {}
    for word in tuple:
        if not(word in some_dict):
            some_dict[word] = 1
        else:
            some_dict[word] = some_dict[word] + 1
    return some_dict

def average_prices(collection):
    total_price = {}
    total_number = {}
    for commodity, price in collection:
        if not(commodity in total_price):
            total_price[commodity] = price
            total_number[commodity] = 1
        else:
            total_price[commodity] = total_price[commodity] + price
            total_number[commodity] = total_number[commodity] + 1
    averages = {}
    for commodity in total_price:
        averages[commodity] = total_price[commodity] / total_number[commodity]
    return averages

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(tuple):
    some_dict = {}
    for i in range(1, len(tuple)):
        bigram = tuple[i - 1], tuple[i]
        if not(bigram in tuple):
            some_dict[bigram] = 1
        else:
            some_dict[bigram] = some_dict[bigram] + 1
    return some_dict