# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(strings):
    dict = {}
    for str in strings:
        if str not in dict:
            dict[str] = 1
        else:
            dict[str] += 1
    return dict


def average_prices(commodities):
    totaldict = {}
    countdict = {}
    for item in commodities:
      
        if item[0] not in totaldict:
            totaldict[item[0]] = item[1]
            countdict[item[0]] = 1
        else:
            totaldict[item[0]] += item[1]
            countdict[item[0]] += 1
    finaldict = {}
    for item in totaldict:
        finaldict[item] = totaldict[item]/countdict[item]
    return finaldict

def count_bigrams(strings):
    bigram_total = []
    dict = {}
    for i in range(0, len(strings)-1):
        bigram = (strings[i], strings[i+1])
        bigram_total.append(bigram)
    for item in bigram_total:
        if item not in dict:
            dict[item] = 1
        else:
            dict[item] += 1
    return dict

