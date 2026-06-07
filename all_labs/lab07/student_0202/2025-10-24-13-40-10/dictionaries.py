# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tup):
    word_dict = {}
    for word in tup:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict

def average_prices(commod):
    total_price_dict = {}
    total_dict = {}
    average_price_dict = {}
    for i in commod:
        if i[0] not in total_price_dict:
            total_price_dict[i[0]] = i[1]
            total_dict[i[0]] = 1
        else:
            total_price_dict[i[0]] += i[1]
            total_dict[i[0]] += 1
    for i in total_price_dict:
        average_price_dict[i] = total_price_dict[i]/total_dict[i]
    return average_price_dict

def count_bigrams(tup):
    i = 0
    bigram_dict = {}

    while True:
        if i > len(tup)-2:
            break
        if tup[i] + tup[i+1] not in bigram_dict:
            bigram_dict[(tup[i], tup[i+1])] = 1
        else:
            bigram_dict[(tup[i], tup[i+1])] += 1
        i+=1
    return bigram_dict

print(count_bigrams(('this', 'is', 'a', 'test', 'this', 'is')))

