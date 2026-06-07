# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(stringTuple):
    freqDict = {}
    for word in stringTuple:
        if word in freqDict:
            freqDict[word] += 1
        else:
            freqDict[word] = 1
    return freqDict

def average_prices(commodityPrices):
    averagePriceDict = {}
    for item in commodityPrices:
        if item[0] in averagePriceDict:
            averagePriceDict[item[0]].append(item[1])
        else:
            averagePriceDict[item[0]] = [item[1]]
    for item in averagePriceDict:
        averagePriceDict[item] = sum(averagePriceDict[item]) / len(averagePriceDict[item])
    return averagePriceDict

def count_bigrams(stringTuple):
    bigramFreqDict = {}
    for i in range(len(stringTuple) -1):
        if (stringTuple[i], stringTuple[i+1],) in bigramFreqDict:
            bigramFreqDict[(stringTuple[i], stringTuple[i+1],)] += 1
        else:
            bigramFreqDict[(stringTuple[i], stringTuple[i+1],)] = 1
    return bigramFreqDict
