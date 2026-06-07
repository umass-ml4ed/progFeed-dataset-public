# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(x):
    d={}
    for word in x:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
    return d

def average_prices(x):
    total_price={}
    total_number={}
    for item in x:
        if item[0] in total_price:
            total_price[item[0]]+=item[1]
            total_number[item[0]]+=1
        else:
            total_price[item[0]]=item[1]
            total_number[item[0]]=1
    d={}
    for item in total_price:
        if item in d:
            continue
        else:
            d[item]=total_price[item]/total_number[item]
    return d

def count_bigrams(x):
    d={}
    for word in range(len(x)-1):
        if x[word:word+2] in d:
            d[x[word:word+2]]+=1
        else:
            d[x[word:word+2]]=1
    return d