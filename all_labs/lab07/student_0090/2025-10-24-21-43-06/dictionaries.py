# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    some_dict = {}
    
    for word in words:
        if word not in some_dict:
            some_dict[word] = 0
        if word in some_dict:
            some_dict[word] +=1
    return some_dict

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(prices):
    total_price = {}
    total_number = {}
    for commodity_name, price in prices:
        if commodity_name not in total_number:
            total_number[commodity_name] = 0
            total_price[commodity_name] = 0
        total_number[commodity_name] += 1
        total_price[commodity_name] += price
    result = {}
    for commodity_name in total_number:
        result[commodity_name] = total_price[commodity_name] / total_number[commodity_name]
    return result
    
    
def count_bigrams(words):
    bigram_dict = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram not in bigram_dict:
            bigram_dict[bigram] = 0
        bigram_dict[bigram] += 1
    return bigram_dict   

        
