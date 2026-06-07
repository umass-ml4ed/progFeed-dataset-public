# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(word_list):
    words_dict = {}
    for w in word_list:
        if w in words_dict:
            words_dict[w] += 1
        else:
            words_dict[w] = 1
    return words_dict

def average_prices(prices):
    total_price_dict = {}
    total_number_dict = {}
    for item in prices:
        name = item[0]
        price = item[1]
        if name in total_price_dict:
            total_price_dict[name] += price
            total_number_dict[name] += 1
        else:
            total_price_dict[name] = price
            total_number_dict[name] = 1

    average_price_dict = {}
    for item in total_price_dict:
        average_price_dict[item] = total_price_dict[item] / total_number_dict[item]

    return average_price_dict

def count_bigrams(words):
    bigram_dict = {}
    for b in range(len(words) - 1):
        bigram = (words[b], words[b + 1])
        if bigram in bigram_dict:
            bigram_dict[bigram] += 1
        else:
            bigram_dict[bigram] = 1
    return bigram_dict
