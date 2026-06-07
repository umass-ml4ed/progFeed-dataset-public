# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    new={}
    for i in words:
        if i in new:
            new[i]+=1
        else:
            new[i]=1
    print(new)

def average_prices(prices):
    total_prices = {}
    counts = {}
    for commodity, price in prices:
        if commodity in total_prices:
            total_prices[commodity] += price
            counts[commodity] += 1
        else:
            total_prices[commodity] = price
            counts[commodity] = 1
    averages = {commodity: total_prices[commodity] / counts[commodity] for commodity in total_prices}
    
    return averages

def count_bigrams(words):
    bigram_counts = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts