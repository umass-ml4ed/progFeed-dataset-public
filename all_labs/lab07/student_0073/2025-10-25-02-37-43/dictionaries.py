# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    some_dict = {}
    for i in words:
        if i not in some_dict:
            some_dict[i] = 1
        else:
            some_dict[i] += 1 
    return some_dict 

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(prices):
    totals = {}
    for name, price in prices:
        if name in totals:
            totals[name][0] += price
            totals[name][1] += 1
        else:
            totals[name] = [price,1]
    averages = {}
    for name in totals: 
        total_price = totals[name][0]
        count = totals[name][1]
        averages[name] = total_price / count
    return averages



prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))


def count_bigrams(words):
    some_dict = {}
    if len(words) < 2:
        return {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in some_dict:
            some_dict[bigram] += 1
        else: 
            some_dict[bigram] = 1   
    return some_dict


print(count_bigrams(()))         
print(count_bigrams(('hello',))) 
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))