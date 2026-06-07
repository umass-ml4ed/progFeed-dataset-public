# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw') 
def count_words(words):
    some_dict = {}
    for word in words:
        if word in some_dict:
            some_dict[word]+=1
        else:
            some_dict[word] =1
    return some_dict


prices = (('gouda cheese 1 lbs', 3.49), ('organic oyster mushroom 1 lbs', 6.89), ('toilet paper 1 roll', 3.99), ('apple juice 1 gallon', 7.99), ('gouda cheese 1 lbs', 4.29), ('toilet paper 1 roll', 4.19), ('talenti gelato vanilla', 5.59))

def average_prices(prices):
    totals = {}
    counts ={}
    for item, price in prices:
        if item in totals:
            totals[item] += price
            counts[item] += 1
        else:
            totals[item] = price
            counts[item] = 1
    return {item: totals[item] / counts[item] for item in totals}

words2 = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
def bigram_counts(words2):
    counts = {}
    number = len(words2)
    for i in range(number - 1):
        bigrams = (words2[i], words2[i + 1])
        if bigrams in counts:
            counts[bigrams] += 1
        else:
            counts[bigrams] = 1
    return counts

print(count_words(words))
print(average_prices(prices))
print(bigram_counts(words2))
