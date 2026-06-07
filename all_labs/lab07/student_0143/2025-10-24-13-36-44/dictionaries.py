# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    dictionary = {}
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

def average_prices(items):
    count = {}
    total_price = {}
    average_price = {}
    for item in items:
        if item[0] in count:
            count[item[0]] += 1
        else:
            count[item[0]] = 1
    for price in items:
        if price[0] in total_price:
            total_price[price[0]] += price[1]
        else:
            total_price[price[0]] = price[1]
    for item in count:
        average_price[item] = total_price[item] / count[item]
    return average_price

def count_bigrams(list_words):
    bigram_count = {}
    for n in range(len(list_words) - 1):
        if (list_words[n],list_words[n+1]) in bigram_count:
            bigram_count[(list_words[n],list_words[n+1])] += 1
        else:
            bigram_count[(list_words[n],list_words[n+1])] = 1
    return bigram_count

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))