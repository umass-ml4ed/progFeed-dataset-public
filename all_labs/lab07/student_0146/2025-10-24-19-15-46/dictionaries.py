# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tuple):
    d = {}
    for word in tuple:
        if word not in d:
            d[word] = 1
        elif word in d:
            d[word] += 1
    return d

def average_prices(input):
    price = {}
    number = {}
    for item, value in input:
        if item not in price:
            price[item] = value
            number[item] = 1
        else:
            price[item] += value
            number[item] += 1
    averages = {}
    for item in price:
        averages[item] = price[item] / number[item]
    return averages

# prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
# print(average_prices(prices))

def count_bigrams(tuple):
    unique = {}
    if len(tuple) < 2:
        return {}
    for i in range(len(tuple) - 1):
        new = (tuple[i], tuple[i + 1])
        if new not in unique:
            unique[new] = 1
        else:
            unique[new] += 1
    return unique

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))