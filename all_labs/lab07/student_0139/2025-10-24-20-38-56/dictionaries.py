# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(a):
    dict1={}
    for i in a:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    return dict1
# words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
# print(count_words(words))

def average_prices(prices):
    total = {}
    count = {}
    
    for commodity, price in prices:
        if commodity in total:
            total[commodity] += price
            count[commodity] += 1
        else:
            total[commodity] = price
            count[commodity] = 1

    averages = {item: total[item] / count[item] for item in total}
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
