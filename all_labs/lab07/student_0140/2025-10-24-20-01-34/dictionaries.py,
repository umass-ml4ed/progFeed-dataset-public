# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(word_tuple): 
    some_dict = {}
    for word in word_tuple:
        if word in some_dict:
            some_dict[word] += 1
        else:
            some_dict[word] = 1
    return some_dict    

def average_prices(price_tuple):
    price_dict = {}
    for item, price in price_tuple:
        if item in price_dict:
            price_dict[item].append(price)
        else:
            price_dict[item] = [price]
    
    for item in price_dict:
        avg_price = sum(price_dict[item]) / len(price_dict[item])
        price_dict[item] = avg_price
    
    return price_dict

def count_bigrams(bigram_tuple):
    bigram_dict = {}
    for i in range(len(bigram_tuple) -1):
        bigram = (bigram_tuple[i], bigram_tuple[i+1])
        if bigram in bigram_dict:
            bigram_dict[bigram] += 1
        else:
            bigram_dict[bigram] = 1
    return bigram_dict




   