# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words (s):
    some_dict = {}
    for i in s:
        if i not in some_dict:
            some_dict[i] = 1
        else:
            some_dict[i] += 1 
    return some_dict
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
#print(count_words(words))

def average_prices (t):
    count = {}
    sums = {}
    for item, price in t:
        if item not in sums:
            sums[item] = price
            count[item] = 1
        else:
            sums[item] += price
            count[item] += 1
    averages = {}
    for item in sums:
        averages[item] = sums[item]/count[item]
    return averages
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
#print(average_prices(prices))

def count_bigrams (s):
    some_dict = {}
    for i in s:
        if i not in some_dict:
            some_dict[i] + some_dict[i+1] = 1
        else:
            some_dict[i], some_dict[i+1] += 1
    return some_dict
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))
