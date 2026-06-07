# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

def count_words(words):
    some_dict = {}
    for word in words:
        if word in some_dict:
            some_dict[word] += 1
        else:
            some_dict[word] = 1
    return some_dict
    
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))


def average_prices(prices):
    total_price = {}
    total_number = {}
    average = {}
    for commodity, price in prices:
        if commodity in total_price:
            total_price[commodity] += price
            total_number[commodity] += 1
        else:
            total_price[commodity] = price
            total_number[commodity] = 1
        average[commodity] = ((total_price[commodity])/(total_number[commodity]))
    return average

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))


def count_bigrams(words):
    some_dict = {}
    for word in range(len(words) -1):
        bigram = (words[word], words[word + 1])
        if bigram in some_dict:
            some_dict[bigram] += 1
        else:
            some_dict[bigram] = 1
    return some_dict

count_bigrams(())         # returns {}
count_bigrams(('hello',)) # returns {} (note the trailing comma, which indicates
                          # this is a 1-element tuple instead of just a string)
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

