# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    count = {}
    for i in words:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    return count
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(prices):
    tp = {}
    tn = {}
    for i, price in prices:
        if i in tp:
            tp[i] += price
            tn[i] += 1
        else:
            tp[i] = price
            tn[i] = 1
    average = {}
    for i in tp:
        average[i] = round(tp[i] / tn[i], 1)
    return average
    
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(wrds):
    count = {}
    for i in range(len(wrds) - 1):
        bigram = (wrds[i], wrds[i+1])
        if bigram in count:
            count[bigram] += 1
        else:
            count[bigram] = 1
    return count
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))



