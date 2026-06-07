# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tuple):
    some_dict = {}
    for word in tuple:
        if word not in some_dict:
            some_dict[word] = 1
        else:
            some_dict[word] += 1
    return some_dict

def average_prices(tuple):
    total_prices_dict = {}
    items_count_dict = {}
    average_prices_dict = {}
    for item in tuple:
        if item[0] not in total_prices_dict:
            total_prices_dict[item[0]] = item[1]
            items_count_dict[item[0]] = 1
        else:
            total_prices_dict[item[0]] = total_prices_dict[item[0]] + item[1]
            items_count_dict[item[0]] += 1
    for item in total_prices_dict:
        average_prices_dict[item] = total_prices_dict[item] / items_count_dict[item]
    return average_prices_dict

def count_bigrams(tuple):
    some_dict = {}
    bigram_list = []
    tuple_index = 0
    for word in tuple:
        try:
            bigram_list.append((word, tuple[tuple_index + 1]))
            tuple_index += 1
        except:
            break
    for bigram in bigram_list:
        if bigram not in some_dict:
            some_dict[bigram] = 1
        else:
            some_dict[bigram] += 1
    return some_dict
