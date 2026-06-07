# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(tuple):
    some_dict = {}
    for word in tuple:
        if word in some_dict:
            some_dict[word] += 1
        else:
            some_dict[word] = 1
    return some_dict

def average_prices(tuple):
    total_prices ={}
    total_counts = {}
    for commodity, price in tuple:
        if commodity in total_prices:
            total_prices[commodity] += price
            total_counts[commodity] += 1
        else:
            total_prices[commodity] = price
            total_counts[commodity] = 1
    averages = {}
    for commodity in total_prices:
        averages[commodity] = total_prices[commodity]

    return averages