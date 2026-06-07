# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    diction = {} 
    for n in words:
        if n not in diction:
            diction[n] = 1
        else:
            diction[n] += 1
    return diction

def average_prices(price):
    prices = {}

    for item in price:
        if item[0] in prices:
            prices[item[0]].append(item[1])
        else:
            prices[item[0]] = [item[1]]
    for key in prices:
        prices[key] = sum(prices[key]) / len(prices[key])
    return prices
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))





