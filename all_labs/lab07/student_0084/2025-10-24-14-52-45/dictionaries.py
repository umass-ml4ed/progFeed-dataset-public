# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    some_dict = {}
    for k in words:
        if k not in some_dict:
            some_dict[k] = 1
        else:
            some_dict[k] += 1
    return some_dict

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(prices):
    total_prices = {}
    total_number = {}
    for commodity, price in prices:
        if commodity in total_prices:
            total_prices[commodity] += price
            total_number[commodity] += 1
        else:
            total_prices[commodity] = price
            total_number[commodity] = 1
    average = {}
    for commodity in total_prices:
        average[commodity] = total_prices[commodity] / total_number[commodity]
    return average

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(words):
    some_dict = {}
    if len(words) < 2:
        return some_dict
    previous_word = words[0]
    for current_word in words[1:]:
        bigram = (previous_word, current_word)
        if bigram in some_dict:
            some_dict[bigram] += 1
        else: 
            some_dict[bigram] = 1
        previous_word = current_word
    return some_dict

count_bigrams(())         # returns {}
count_bigrams(('hello',)) # returns {} (note the trailing comma, which indicates
                          # this is a 1-element tuple instead of just a string)

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))