# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(strings):
    some_dict = {}
    for i in strings:
        if i not in some_dict:
            some_dict[i] = 1
        else:
            some_dict[i] += 1
    
    return some_dict

def average_prices(tple):
    total_price = {}
    total_number = {}
    for name, price in tple:
        if name not in total_number:
            total_price[name] = price
            total_number[name] = 1
        else:
            total_price[name] += price
            total_number[name] += 1
        
    average_prices = {}
    for name in total_price:
        average_prices[name] = total_price[name] / total_number[name]
    
    return average_prices

def count_bigrams(tple):
    some_dict = {}
    if len(tple) < 2:
        return some_dict
    for i in range(0, len(tple) - 1):
        bigram = (tple[i], tple[i + 1])
        if bigram not in some_dict:
            some_dict[bigram] = 1
        else:
            some_dict[bigram] += 1
    
    return some_dict
        
    

        


        


