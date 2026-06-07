# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

def count_words(words):
    some_dict = {}
    for word in words:
        if word in some_dict:
            some_dict[word] += 1
        else:
            some_dict[word] = 1
    return some_dict
    
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))


def average_prices(prices):
    total_price = {}
    total_number = {}
    average = {}
    for commodity, price in prices:
        if commodity in total_price:
            total_price[commodity] += price
            total_number[commodity] += 1
        else:
            total_price[commodity] = price
            total_number[commodity] = 1
        average[commodity] = ((total_price[commodity])/(total_number[commodity]))
    return average

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))




