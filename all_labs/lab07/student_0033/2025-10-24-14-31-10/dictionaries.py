# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(t):
    some_dict={}
    for i in t:
        if i in some_dict:
            some_dict[i]+=1
        else:
            some_dict[i]=1
    return some_dict

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))


def average_prices(t):
    sums = {}
    counts = {}
    for commodity, price in t:
        if commodity in sums:
            sums[commodity] += price
            counts[commodity] += 1
        else:
            sums[commodity] = price
            counts[commodity] = 1

    averages = {}
    for commodity in sums:
        averages[commodity] = sums[commodity] / counts[commodity]
    return averages

def count_bigrams(t):
    bigram_dict = {}
    for i in range(len(t) - 1):
        bigram = (t[i], t[i + 1])
        if bigram in bigram_dict:
            bigram_dict[bigram] += 1
        else:
            bigram_dict[bigram] = 1
    return bigram_dict





