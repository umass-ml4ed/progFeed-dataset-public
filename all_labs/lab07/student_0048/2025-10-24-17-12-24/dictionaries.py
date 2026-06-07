# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


def count_words(words):
    dict = {}
    for i in words:
        x = 1
        if i not in dict:
            dict[i] = x
        else:
            dict[i]=dict[i]+1
    return dict
        

def average_prices(prices):
    base = {}
    avg = {}
    total = {}
    for i in prices:
        if i[0] not in base:
            base[i[0]]=1
            avg[i[0]]=i[1]
        else:
            base[i[0]]+=1
            avg[i[0]]=avg[i[0]]+i[1]
    for i in avg:
        total[i]=avg[i]/base[i]
    return total


def count_bigrams(bigrams):
    combs = {}
    for i in bigrams:
        x = 1
        if i+(i+1) not in combs:
            combs[i] = x
        else:
            combs[i]=combs[i]+1
    return combs





