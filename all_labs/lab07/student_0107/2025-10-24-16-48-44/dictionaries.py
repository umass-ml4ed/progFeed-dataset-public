# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(tup):
    d = {}
    for word in tup:
        if word in d:
            d[word] = d[word] + 1 
        if word not in d:
            d.update({word:1})
        

    return d



def average_prices(price_list):
    d = {}
    for item in price_list:
        for thing in item:
            d.update({item[0]:thing})
   #     if item in price_list:
             
    return d


def count_bigrams(tup):
    d = {}
    if len(tup) == 1:
        return d 
    
    for i in range(0,len(tup)-1):
        item = tup[i],tup[i+1]
        if item not in d:
            d.update({item:0})
        if item in d:
            d[item] = d[item] +1
    return d

#words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
#print(count_words(words))
#Output → {'he': 1, 'saw': 4, 'a': 2}

#p = (('gouda cheese 1 lbs', 3.49), ('organic oyster mushroom 1 lbs', 6.89), ('toilet paper 1 roll', 3.99), ('apple juice 1 gallon', 7.99), ('gouda cheese 1 lbs', 4.29), ('toilet paper 1 roll', 4.19), ('talenti gelato vanilla', 5.59))
#print(average_prices(p))

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

#Output → {('she', 'knows'): 3, ('knows', 'and'): 1, ('and', 'she'): 1, ('knows', 'that'): 2, ('that', 'he'): 1, ('he', 'knows'): 1, ('that', 'she'): 1}
