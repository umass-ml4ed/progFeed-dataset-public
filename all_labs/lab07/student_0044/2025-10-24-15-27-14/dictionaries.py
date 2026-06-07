# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(x):
    d={}
    for a in x:
        if a not in d:
            d[a]=1
        else:
            d[a]+=1
    return(d)
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(x):
    d1={}
    d2={}
    d3={}
    for n,p in x:
        if n in d1:
            d1[n]+=1
            d2[n]+=p
        else:
            d1[n]=1
            d2[n]=p
    for a in d1:
        d3[a]=d2[a]/d1[a]
    return(d3)
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(x):
    some_dict = {}
    for a in range(0, len(x)-1):
        bigram=(x[a], x[a+1])
        if bigram not in some_dict:
            some_dict[bigram]=1
        else:
            some_dict[bigram]+=1
    return(some_dict)
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))