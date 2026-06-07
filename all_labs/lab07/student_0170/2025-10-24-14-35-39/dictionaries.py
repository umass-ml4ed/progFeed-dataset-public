# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(strings):
    some_dict = {}
    for s in strings:
        if s in some_dict:
            some_dict[s] += 1
        else:
            some_dict[s] = 1
    return some_dict

def average_prices(prices):
    total = {}
    for t in prices:
        if t[0] in total:
            total[t[0]].append(t[1])
        else:
            total[t[0]] = [t[1]]
    for key in total:
        value = total[key]
        items = len(value)
        total[key] = sum(value)/items
    return total

def count_bigrams(words):
    bigrams = {}
    for i in range(len(words)-1):
        t = (words[i],words[i+1])
        if t in bigrams:
            bigrams[t] += 1
        else:
            bigrams[t] = 1
    return bigrams
