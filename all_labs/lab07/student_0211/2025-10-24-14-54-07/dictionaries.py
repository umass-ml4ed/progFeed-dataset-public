# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(t : tuple):
    some_dict = {}
    for s in t:
        if s in some_dict:
            some_dict[s] += 1
        else:
            some_dict[s] = 1
    return some_dict

def average_prices(prices : tuple):
    price_dict = {}
    count = {}
    for t in prices:
        item = t[0]
        price = t[1]
        if item in price_dict:
            price_dict[item] += price
            count[item] += 1
        else:
            price_dict[item] = price
            count[item] = 1
    for item in price_dict:
        price_dict[item] = price_dict[item] / count[item]
    return price_dict

# def count_bigrams(t: tuple):
#     some_dict = {}
#     for i in range(len(t)):
#         two_words = 


# prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
# print(average_prices(prices))

# words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
# print(count_words(words))