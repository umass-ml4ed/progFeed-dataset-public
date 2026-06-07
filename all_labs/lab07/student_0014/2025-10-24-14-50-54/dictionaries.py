# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(count):
    dict = {}
    for i in count:
        if i not in count:
            dict[count] = 1
        else:
            dict[count] += 1
    return dict
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
            tn = 1
    average = {}
    for i in tp:
        average[i] = round(tp[i] / tn[i], 1)
        return average
    
     
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

