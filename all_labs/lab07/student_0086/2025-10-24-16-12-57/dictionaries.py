# Author : REDACTED
# Email  : REDACTED
# SpireID: REDACTED


def count_words(words):
    some_dict = {}
    for word in words:
        if word in some_dict:
            some_dict[word] += 1
        else:
            some_dict[word] = 1
    return some_dict

        

def average_prices(prices_tuple):
    total_prices = {}
    counts = {}
    
    for name, price in prices_tuple:
        if name in total_prices:
            total_prices[name] += price
            counts[name] += 1
        else:
            total_prices[name] = price
            counts[name] = 1
    
    averages = {}
    for name in total_prices:
        averages[name] = total_prices[name] / counts[name]
    
    return averages



def count_bigrams(words_tuple):
    some_dict = {}
    
    if len(words_tuple) < 2:
        return some_dict
    
    for i in range(len(words_tuple) - 1):
        bigram = (words_tuple[i], words_tuple[i + 1])
        if bigram in some_dict:
            some_dict[bigram] += 1
        else:
            some_dict[bigram] = 1
    
    return some_dict
