# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words)->dict:
    some_dict = {}
    for i in words:
        if i in some_dict:
            some_dict[i]+=1
        else:
            some_dict[i]=1
    return some_dict

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(tup):
    CPIprice={}
    CPInum={}
    result={}
    for i, price in tup:
        if i in CPIprice:
            CPInum[i]+=1
            CPIprice[i]+=price
        else:
            CPInum[i]=1
            CPIprice[i]=price

    for i in CPIprice:
        result[i]=CPIprice[i]/CPInum[i]
    return result


prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(word)-> dict:
    some_dict={}
    if len(word)<2:
        return some_dict

    for i in range(0,len(word)-1):
        item = word[i],word[i+1]
        if item not in some_dict:
            some_dict[item] = 1
        else:
            some_dict[item]+=1
    return some_dict
            

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))