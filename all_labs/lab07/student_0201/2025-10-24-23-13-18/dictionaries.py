# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words (words):
    some_dict = {}
    for word in words:
        if word in some_dict:
            some_dict[word] += 1
        else:
            some_dict[word] = 1
    return some_dict

def average_prices(prices):
    some_dict = {}
    for commodity, price in prices:
        if commodity in some_dict:
            some_dict[commodity].append(price)
        else:
            some_dict[commodity] = [price]
    for commodity in some_dict:
        average = sum(some_dict[commodity])/len(some_dict[commodity])
        some_dict[commodity] = average
    return some_dict

def count_bigrams(words):
    some_dict = {}
    if len(words)<2:
        return some_dict
    for i in range(len(words)-1):
        bigram = (words[i], words[i+1])
        if bigram in some_dict:
            some_dict[bigram] += 1
        else:
            some_dict[bigram] = 1

    return some_dict
