# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
import math
import random
def count_words(words):
    a_dict={}
    for word in words:
        if word in a_dict:
            a_dict[word]+=1
        else:
            a_dict[word]=1
    return a_dict

def average_prices(commo):
    commo_prices={}
    for name, price in commo:
        if name in commo_prices:
            commo_prices[name].append(price)
        else:
            commo_prices[name]=[price]
    avg_price={}
    for name, price_list in commo_prices.items():
        avg_price[name]= float(sum(price_list))/float(len(price_list))
    return avg_price

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))