# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def count_words(words):
    words_count = {}
    for word in words:
        word = word.lower()
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    return words_count

def average_prices(prices):
    totals = {}
    count = {}
    for name,price in prices:
        name=name.lower()
        if name in totals:
            totals[name] += price
            count[name]+= 1
        else:
            totals[name]=price
            count[name] = 1
    return {name: totals[name]/ count[name] for name in totals}

def count_bigrams(words):
    bigram_count={}
    for i in range(len(words)-1):
        bigram = (words[i].lower(), words[i + 1].lower())
        if bigram in bigram_count:
            bigram_count[bigram]+=1
        else:
            bigram_count[bigram]=1
    return bigram_count