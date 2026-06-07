# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    some_dict={}
    for i in words:
        if i in some_dict:
            some_dict[i]+=1
        else:
            some_dict[i]=1
    return some_dict
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(items):
    totals={}
    a={}
    for name,price in items:
        if name in totals:
            totals[name]+=price
            a[name]+=1
        else:
            totals[name]=price
            a[name]=1
    averages={}
    for name in totals:
        averages[name]=totals[name]/a[name]
    return averages
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(words):
    some_dict={}
    if len(words)<2:
        return some_dict
    i=0
    while i<len(words)-1:
        b=(words[i], words[i+1])
        if b in some_dict:
            some_dict[b]+=1
        else:
            some_dict[b]=1
        i+=1
    return some_dict
print(count_bigrams(()))           
print(count_bigrams(('hello',)))
words = ('she','knows','and','she','knows','that','he','knows','that','she','knows')
print(count_bigrams(words))