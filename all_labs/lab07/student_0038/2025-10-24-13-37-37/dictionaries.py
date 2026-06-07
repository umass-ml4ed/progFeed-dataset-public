# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(words_list:tuple):
    some_dict = {}
    for string in words_list:
        if string in some_dict:
            some_dict[string] += 1
        else:
            some_dict[string] = 1
    return some_dict

def average_prices(commodity_info):
    total_prices = {}
    total_number = {}
    item_average = {}
    for item in commodity_info:
        commodity_name = item[0]
        commodity_price = item[1]
        if commodity_name in total_prices:
            total_prices[commodity_name] += commodity_price
        else:
            total_prices[commodity_name] = commodity_price
        if commodity_name in total_number:
            total_number[commodity_name] += 1
        else:
            total_number[commodity_name] = 1
    for name in total_prices:
        item_average[name] = total_prices[name] / total_number[name]
    return item_average

def count_bigrams(words_list:tuple):
    some_dict = {}
    for i in range(len(words_list)-1):
        bigram = (words_list[i], words_list[i+1])
        if bigram in some_dict:
            some_dict[bigram] += 1
        else:
            some_dict[bigram] = 1
    return some_dict

