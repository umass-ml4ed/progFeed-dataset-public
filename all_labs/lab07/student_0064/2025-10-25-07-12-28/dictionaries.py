# Author  : REDACTED
# Email : REDACTED
# Spire ID  : REDACTED

def count_words(words):
    some_dict = {}

    for word in words:
        if word not in some_dict:
            some_dict[word] = 1
        else:
            some_dict[word] += 1

    return some_dict

  
    
def average_prices(commodities):
    allprices = {}
    counts = {}
    for name, price in commodities:
        if name not in allprices:
            allprices[name] = price
            counts[name] = 1
        else:
            allprices[name] += price
            counts[name] += 1

    averages = {}
    for name in allprices:
        averages[name] = allprices[name] / counts[name]

    return averages

def count_bigrams(words):

    fullbigram = {}

    if len(words) < 2:
        return {}

    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram not in fullbigram:
            fullbigram[bigram] = 1
        else:
            fullbigram[bigram] += 1

    return fullbigram