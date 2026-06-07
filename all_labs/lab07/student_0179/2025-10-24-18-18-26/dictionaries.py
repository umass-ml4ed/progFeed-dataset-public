# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    some_dict = {}
    for word in words:
        if word not in some_dict:
            some_dict[word] = 1
        else:
            some_dict[word] += 1
    return some_dict

def average_prices(commodities_prices):
    total_prices = {}
    total_numbers = {}
    average = {}
    for commodity_price in commodities_prices:
        if commodity_price[0] not in total_prices and commodity_price not in total_prices:
            total_prices[commodity_price[0]] = commodity_price[1]
            total_numbers[commodity_price[0]] = 1
        else:
            total_prices[commodity_price[0]] += commodity_price[1]
            total_numbers[commodity_price[0]] += 1
    for total_price in total_prices:
        if total_price in total_numbers:
            average[total_price] = total_prices[total_price] / total_numbers[total_price]
    return average

def count_bigrams(words):
    some_dict = {}
    for word in words:
        if (word,words[words.index(word) + 1]) not in some_dict:
            some_dict[(word, words[words.index(word) + 1])] = 1
        else:
            some_dict[(word, words[words.index(word) + 1])] += 1
    return some_dict

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

