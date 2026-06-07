# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def count_words(a):
    some_dict={}
    for b in a:
        if b in some_dict:
            some_dict[b]=some_dict[b]+1
        else:
            some_dict[b]=1
    return some_dict

def average_prices(a):
    result={}
    for name,price in a:
        if name in result:
            result[name].append(price)
        else:
            result[name]=[price]
    for name in result:
        result[name] = sum(result[name])/len(result[name])       
    return result

def count_bigrams(words):
    bigram_counts = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
            
    return bigram_counts   


















