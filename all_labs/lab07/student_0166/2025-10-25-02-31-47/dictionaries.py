# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(list_of_words):
    some_dict = {}
    for i in list_of_words:
        if i not in some_dict:
            some_dict[i] = 1
        else:
            some_dict[i] += 1
    return some_dict


def average_prices(prices):
    total_price = {}
    total_number = {}

    for letter, num in prices:
        if letter not in total_price:
            total_price[letter] = num
            total_number[letter] = 1
        else:
            total_price[letter] += num
            total_number[letter] += 1
    
    average = {}
    for letter in total_price:
        average[letter] = total_price[letter]/total_number[letter]
    
    return average


def count_bigrams(item):
    if len(item) < 2:
        return {}
    
    some_dict = {}

    for i in range(len(item) - 1):
        bigram = (item[i], item[i+1])
        if bigram in some_dict:
            some_dict[bigram] += 1
        else:
            some_dict[bigram] = 1
    return some_dict