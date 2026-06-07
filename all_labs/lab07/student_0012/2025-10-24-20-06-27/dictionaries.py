# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tup1):
    word_count = {}
    for word in tup1:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count  

def average_prices(tup2):
    price_dict = {}
    count_dict = {}
    for item, price in tup2:
        if item in price_dict:
            price_dict[item] += price
            count_dict[item] += 1
        else:
            price_dict[item] = price
            count_dict[item] = 1
    avg_price_dict = {item: price_dict[item] / count_dict[item] for item in price_dict}
    return avg_price_dict

def count_bigrams(tup3):
    some_dict = {}
    for i in range(len(tup3) - 1):
        bigram = (tup3[i], tup3[i + 1])
        if bigram in some_dict:
            some_dict[bigram] += 1
        else:
            some_dict[bigram] = 1
    return some_dict

print(count_bigrams(('hello',)))