# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def count_words(words_tuple):
    word_count = {}
    for word in words_tuple:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def average_prices(prices_tuple):
    price_dict = {}
    count_dict = {}
    
    for commodity, price in prices_tuple:
        if commodity in price_dict:
            price_dict[commodity] += price
            count_dict[commodity] += 1
        else:
            price_dict[commodity] = price
            count_dict[commodity] = 1
    
    average_dict = {}
    for commodity in price_dict:
        average_dict[commodity] = price_dict[commodity] / count_dict[commodity]
    
    return average_dict


def count_bigrams(words_tuple):
    bigram_count = {}
    for i in range(len(words_tuple) - 1):
        bigram = (words_tuple[i], words_tuple[i + 1])
        if bigram in bigram_count:
            bigram_count[bigram] += 1
        else:
            bigram_count[bigram] = 1
    return bigram_count
