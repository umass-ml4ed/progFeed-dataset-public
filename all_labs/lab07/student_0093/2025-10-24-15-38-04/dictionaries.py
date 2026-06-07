# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(words):
    some_dict = {}
    for str in words:
        if str not in some_dict:
            some_dict[str] = 1
        else:
            some_dict[str] += 1
    return some_dict
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))
# Output → {'he': 1, 'saw': 4, 'a': 2}

def average_prices(prices):
    total_price = {}
    total_number = {}
    averages = {}
    for commodity, price in prices:
        if commodity not in total_price:
            total_price[commodity] = price
            total_number[commodity]  = 1
        else:
            total_price[commodity] += price
            total_number[commodity] += 1
    for commodity in total_price:
        averages[commodity] = total_price[commodity] / total_number[commodity]
    return averages
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))
# Output → {'a': 1.1, 'c': 4.2, 'b': 4.0, 'd': 10.4}

def count_bigrams(words):
    some_dict = {}
    for str in range(len(words)):
        bigram = (words[str])
        if bigram not in some_dict:
            some_dict[bigram] = 1
        else:
            some_dict[bigram] += 1
    return some_dict
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))
# Output → {('she', 'knows'): 3, ('knows', 'and'): 1, ('and', 'she'): 1, ('knows', 'that'): 2, ('that', 'he'): 1, ('he', 'knows'): 1, ('that', 'she'): 1}



