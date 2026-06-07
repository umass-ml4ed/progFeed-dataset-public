# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tup):
    some_dict = {}
    for word in tup:
        if word in some_dict:
            some_dict[word] +=1
        else:
            some_dict[word] = 1
    return some_dict

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(tup):
    totalnumber = {}
    totalprice = {}
    for items, prices in tup:
        if items in totalnumber:
            totalnumber[items].append(prices)
        else:
            totalnumber[items] = [prices]
    
    for items, cost in totalnumber.items():
        totalprice[items] = sum(cost)/len(cost)
    return totalprice


prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(words):
    bigram_dict = {}
    for word in range(len(words) - 1):
        bigrams = (words[word], words[word+1])
        if bigrams in bigram_dict:
            bigram_dict[bigrams] += 1
        else:
            bigram_dict[bigrams] = 1
    return bigram_dict

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))








