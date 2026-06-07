# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    some_dict = {}
    for word in words:
        if word not in some_dict:
            some_dict[word] = 1
        else:
            some_dict[word]+=1
    return some_dict

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(tuple):
    average_prices = {}
    price_count = {}

    for commodity, price in tuple:
            if commodity in average_prices:
                 average_prices[commodity]+=price
                 price_count[commodity]+=1
            else:
                average_prices[commodity] = price
                price_count[commodity] = 1

    for commodity in average_prices:
        average_prices[commodity]/=price_count[commodity]

    return average_prices

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))
