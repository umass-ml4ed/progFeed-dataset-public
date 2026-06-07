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

def count_bigrams(s):
    some_dict = {}
    for i in range(len(s) - 1):
        pair = (s[i], s[i + 1])
        if pair not in some_dict:
            some_dict[pair] = 1
        else:
            some_dict[pair] += 1
    return some_dict
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))