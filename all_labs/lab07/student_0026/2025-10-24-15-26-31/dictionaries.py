# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(words):
    dict={}
    for word in words:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    return dict

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(prices):
    totalprice={}
    totalnumber={}
    for item in prices:
        if item[0] not in totalprice:
            totalprice[item[0]]=item[1]
            totalnumber[item[0]]=1
        else:
            totalprice[item[0]]+=item[1]
            totalnumber[item[0]]+=1
    for price in totalprice:
        totalprice[price]=totalprice[price]/totalnumber[price]
    return totalprice

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(words):
    dict={}
    if len(words)<=1:
        dict={}
    else:
        (a, b)= word
        for word in words:
            if word in dict:
                dict[word]+=1
            else: 
                dict[word]=1
    return dict
            

                
