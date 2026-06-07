# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    some_dict = {}
    for word in words:
        if word not in some_dict:
            some_dict[word] = 1
        else:
            some_dict[word] += 1
    return some_dict

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(commodities_prices):
    total_prices = {}
    total_numbers = {}
    average = {}
    for commodity_price in commodities_prices:
        if commodity_price[0] not in total_prices and commodity_price not in total_prices:
            total_prices[commodity_price[0]] = commodity_price[1]
            total_numbers[commodity_price[0]] = 1
        else:
            total_prices[commodity_price[0]] += commodity_price[1]
            total_numbers[commodity_price[0]] += 1
    for total_price in total_prices:
        if total_price in total_numbers:
            average[total_price] = total_prices[total_price] / total_numbers[total_price]
    return average

 
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

