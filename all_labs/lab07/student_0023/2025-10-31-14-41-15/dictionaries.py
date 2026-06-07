# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tup : tuple):
    word_dict = {}

    for i in tup:
        if i not in word_dict:
            word_dict[i] = 1
        else:
            word_dict[i] += 1
    return word_dict

def average_prices(tup):
    avg_price_dict = {}
    for i in tup:
        for j in len(i):
            if j[0] not in avg_price_dict:
                avg_price_dict[j[0]] = j[1]
            else:
                avg_price_dict[j[0]] += j[1]


def average_prices(tup):
    total_price = {}
    count = {}

    for name, price in tup:
        if name in total_price:
            total_price[name] += price
            count[name] += 1
        else:
            total_price[name] = price
            count[name] = 1

    averages = {name: total_price[name] / count[name] for name in total_price}
    return averages

def count_bigrams(words):
    bigram_counts = {}
    
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    
    return bigram_counts



