# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tuple):
    dict={}
    for word in tuple:
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
    return dict

def average_prices(price_tuple):
    pricedict={}
    countdict={}
    for item in price_tuple:
        if item[0] not in pricedict:
            pricedict[item[0]]= item[1]
            countdict[item[0]]=1          
        else:
            pricedict[item[0]]+=item[1]
            countdict[item[0]]+=1
    for element in pricedict:
        pricedict[element]=pricedict[element]/countdict[element]
    return pricedict
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))
            
def count_bigrams(tuple):
    dict={}
    bigram=()
    if len(tuple)<=1:
        dict={}
    else:
        for word in range(0,len(tuple)-1):
            bigram= (tuple[word], tuple[word+1])
            if bigram not in dict:
                dict[bigram]=1
            else:
                dict[bigram]+=1
    return dict
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))