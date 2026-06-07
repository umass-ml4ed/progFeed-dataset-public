# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(list):
    some_dict = {}
    for values in list:
        if values in some_dict:
            some_dict[values] += 1
        else:
            some_dict[values] = 1

    return some_dict

def average_prices(items):
    price_data = {}

    for name, price in items:
        price_data[name]['total'] += price
        price_data[name]['count'] += 1 
    else:
        price_data[name] = {'total': price, 'count':1}

    averages = {}
    for name, data in price_data.items():
        averages[name] = data['total'] / data['count']

    return averages

def count_bigrams(words):
    some_dict = {}

    if len(words) < 2:
        return some_dict
    
    for i in range(len(words) - 1):
        bigram = (words[i], words[i+1])
        if bigram in some_dict:
            some_dict[bigram] += 1 
        else:
            some_dict[bigram] = 1
            
    return some_dict


