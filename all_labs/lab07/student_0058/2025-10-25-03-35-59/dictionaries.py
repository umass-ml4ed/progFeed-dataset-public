# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(words):
    some_dict = {}
    a = 0
    for word in words:
        if word not in some_dict:
            some_dict[word] = 1
        else:
            some_dict[word] += 1
    return some_dict

#words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
#print(count_words(words))

def average_prices(prices):
    
    total_price = {}
    total_count = {}
    for commodity, price in prices:
        total_price[commodity] = total_price.get(commodity, 0) + price
        total_count[commodity] = total_count.get(commodity, 0) + 1
    
    averages = {commodity: total_price[commodity] / total_count[commodity] for commodity in  total_price}
    return averages

#print(average_prices(prices))


def count_bigrams(words):
    some_dict = {}

    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        some_dict[bigram] = some_dict.get(bigram, 0) + 1
    
    return some_dict