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

# commodity_info = (('gouda cheese 1 lbs', 3.49), ('organic oyster mushroom 1 lbs', 6.89), ('toilet paper 1 roll', 3.99), ('apple juice 1 gallon', 7.99), ('gouda cheese 1 lbs', 4.29), ('toilet paper 1 roll', 4.19), ('talenti gelato vanilla', 5.59))
# def average_prices(commodity_info):
#     total_prices = {}
#     total_number = {}
#     for item in commodity_info:

def count_bigrams(words_list:tuple):
    some_dict = {}
    for i in range(len(words_list)-1):
        bigram = (words_list[i], words_list[i+1])
        if bigram in some_dict:
            some_dict[bigram] += 1
        else:
            some_dict[bigram] = 1
    return some_dict

