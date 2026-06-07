# Author : REDACTED
# Email: REDACTED
# Spire ID: REDACTED

#takes a tuple of words as input, and returns a dictionary where the key of each entry is a unique word from the input,
#and the value is the number of times that word appears in the input.
def count_words(words):
    some_dict = {}
    for word in words:
        if word not in some_dict:
            some_dict[word] = 1
        else:
           some_dict[word] += 1
    return some_dict

#a collection of commodities and their prices, and returns a dictionary where the key of each entry is a unique commodity 
#name from the input, and the value is the average price of that commodity. 
def average_prices(prices):
    total_price = {}   
    count = {}

    for commodity, price in prices:
        if commodity not in total_price:
            total_price[commodity] = price
            count[commodity] = 1
        else:
            total_price[commodity] += price
            count[commodity] += 1

    averages = {}   
    for commodity in total_price:
        averages[commodity] = total_price[commodity] / count[commodity]

    return averages

#a tuple of individual words as input, and returns a dictionary where the key of each entry is a unique bigram from the input, 
#and the value is the number of times that bigram occurs
def count_bigrams(words):
    bigram_dict = {}

    if len(words) < 2:
        return bigram_dict
    
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_dict:
            bigram_dict[bigram] += 1
        else:
            bigram_dict[bigram] = 1

    return bigram_dict
