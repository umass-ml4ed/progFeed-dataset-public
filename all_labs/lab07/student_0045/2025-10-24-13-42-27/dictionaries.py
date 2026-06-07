# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def count_words(words):
    result = {}
    for word in words:
        if word in result:
            result[word]+=1
        elif word not in result:
            result[word] = 1
    return result

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(prices):
    result = {}
    item_count = {}
    for item, price in prices:
        if item in result:
            result[item]+=price
            item_count[item]+=1
        else:
            result[item]=price
            item_count[item]=1
    avg_prices_dict = {}
    for item in result:
        avg_prices_dict[item] = result[item]/item_count[item]
    return avg_prices_dict

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))



