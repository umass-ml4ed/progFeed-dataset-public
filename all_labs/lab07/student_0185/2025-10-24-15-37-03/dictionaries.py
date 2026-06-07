# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(t: tuple):
    new_dict = {}
    for word in t:
        if word not in new_dict:
            new_dict[word] = 0
        new_dict[word] += 1
    return new_dict

def average_prices(t: tuple):
    dict_num = {}
    dict_price = {}
    dict_avg_price ={}
    for tup in t:
        if tup[0] not in dict_price:
            dict_price[tup[0]] = tup[1]
            dict_num[tup[0]] = 1
        else:
            dict_price[tup[0]] += tup[1]
            dict_num[tup[0]] += 1
    for tup, value in dict_price.items():
        dict_avg_price[tup] = dict_price[tup]/dict_num[tup]
    return dict_avg_price

def count_bigrams(t: tuple):
    bigram_dict = {}
    for word in range(len(t)-1):
        if (t[word], t[word + 1]) not in bigram_dict:
            bigram_dict[(t[word], t[word + 1])] = (t[word] + t[word + 1])
            bigram_dict[(t[word], t[word + 1])] = 1
        bigram_dict[(t[word], t[word + 1])] += 1
    return bigram_dict