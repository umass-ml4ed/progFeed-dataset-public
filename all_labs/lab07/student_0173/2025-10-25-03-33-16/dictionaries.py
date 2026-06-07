# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(tuple):
    some_dict = {}
    for i in tuple:
        if i in some_dict:
            some_dict[i] += 1
        else:
            some_dict[i] = 1
    return some_dict

def average_prices(tuple):
    avg_dict = {}
    total_dict = {}
    count_dict = {}
    for i in tuple:
        if i[0] in count_dict:
            total_dict[i[0]] += i[1]
            count_dict[i[0]] += 1
        else:
            count_dict[i[0]] = 1
            total_dict[i[0]] = i[1]
    for i in total_dict:
        avg_dict[i] = total_dict[i]/count_dict[i]
    return avg_dict

def count_bigrams(tuple):
    dict = {}
    j = 0
    for i in range(len(tuple)-1):
        j = i+1
        if (tuple[i], tuple[j]) in dict:
            dict[tuple[i], tuple[j]] += 1
        else:
            dict[tuple[i], tuple[j]] = 1
    return dict
