# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(words:tuple):
    some_dict = {}
    for n in words:
        if n in some_dict:
           some_dict[n] += 1
        else: 
              some_dict[n] = 1

    return some_dict

        



def average_prices(commodity:tuple):
    prices_dict = {}
    average_dict ={}
# key = name of the commodity 
# value = list of the prices of ommodity 
# Loop over the input, append the a price to the list of commodity 
# Use the dictionary to teh average price

    for name,price in commodity:
        if name not in prices_dict:
            prices_dict[name] = [price]

        else:
            prices_dict[name].append(price)
    
    for name, prices in prices_dict.items():
        avg = sum(prices)/len(prices)
        average_dict[name] = avg
    return average_dict 

def count_bigrams(word):
    some_dict = {}
    
    for i in range (len(word)-1):
        brigham = word[i], word[i+1]
        if brigham not in some_dict:
            some_dict[brigham] = 1 
        else:
            some_dict[brigham] += 1 
    return some_dict




