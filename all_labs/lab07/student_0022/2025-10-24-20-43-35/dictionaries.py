# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    counted_words = {}
    for word in words:
        if word not in counted_words:
            counted_words[word] = 1
        else:
            counted_words[word] += 1
    return counted_words

def average_prices(commodities):
    average_of_prices = {}
    commodity_counts = {}
    for commodity in commodities:
        if commodity[0] not in average_of_prices:
            average_of_prices[commodity[0]] = commodity[1]
            commodity_counts[commodity[0]] = 1
        else:
            average_of_prices[commodity[0]] += commodity[1]
            commodity_counts[commodity[0]] += 1
    
    for key in average_of_prices:
        average_of_prices[key] = average_of_prices[key]/commodity_counts[key]
    
    return average_of_prices

def count_bigrams(strings):
    bigram_dict = {}
    if len(strings) < 2:
        return bigram_dict
    
    for index in range(len(strings)-1):
        if (strings[index], strings[index+1]) not in bigram_dict:
            bigram_dict[(strings[index], strings[index+1])] = 1
        else:
            bigram_dict[(strings[index], strings[index+1])] += 1
    return bigram_dict

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))