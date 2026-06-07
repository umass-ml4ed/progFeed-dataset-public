# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(in_tuple):
    some_dict = {}
    for word in in_tuple:
        some_dict[f'{word}'] = in_tuple.count(word)
    return some_dict

def average_prices(in_tuple):
    dict1 = {}
    dict2 = {}
    dict3 = {}
    for name, price in in_tuple:
        if name in dict1:
            dict1[name] = dict1[name] + price
            dict2[name] += 1
        else:
            dict1[name] = price
            dict2[name] = 1
        dict3[name] = dict1[name]/dict2[name]
    return dict3

def count_bigrams(in_tuple):
    some_dict = {}
    i = 0
    while i < (len(in_tuple) - 1):
        if (in_tuple[i], in_tuple[i+1]) in some_dict:
            some_dict[(in_tuple[i], in_tuple[i+1])] += 1
        else:
            some_dict[(in_tuple[i], in_tuple[i+1])] = 1
        i += 1
    return some_dict