# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tuple):
    dic = {}
    for word in tuple:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] = dic[word] + 1

    return dic

#words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
#print(count_words(words))

def average_prices(collection):
    total = {}
    count = {}
    for item, price in collection:
        if item not in total:
            total[item] = price
            count[item] = 1
        else:
            total[item] += price
            count[item] += 1

    averages = {}
    for item in total:
        averages[item] = total[item] / count[item]

    return averages

def count_bigrams(tuple):
    dic = {}
    for i in range(len(tuple) -1 ):
        bigram = (tuple[i], tuple[i+1])
        if bigram not in dic:
            dic[bigram] = 1
        else:
            dic[bigram] += 1

    return dic