# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    diction = {} 
    for n in words:
        if n not in diction:
            diction[n] = 1
        else:
            diction[n] += 1
    return diction

def average_prices(price):
    prices = {}
    for item in price:
        if item[0] in prices:
            prices[item[0]].append(item[1])
        else:
            prices[item[0]] = [item[1]]
    for key in prices:
        prices[key] = sum(prices[key]) / len(prices[key])
    return prices

def count_bigrams(words):
    bigrams = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i +1])
        if bigram not in bigrams:
            bigrams[bigram] = 1
        else:
            bigrams[bigram] += 1
    return bigrams    
        





