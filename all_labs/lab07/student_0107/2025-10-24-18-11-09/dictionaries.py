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
        if item[0] not in d:
            d.update({item[0]:item[1]})
        if item[0] in d:
           l = [d[item[0]]]
           l.append(item[1])
           t = sum(l)/len(l)
           d[item[0]] = t 
            



        

    
    
    
             
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

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))
#Output → {'a': 1.1, 'c': 4.2, 'b': 4.0,00] 'd': 10.4}



#words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
#print(count_bigrams(words))

#Output → {('she', 'knows'): 3, ('knows', 'and'): 1, ('and', 'she'): 1, ('knows', 'that'): 2, ('that', 'he'): 1, ('he', 'knows'): 1, ('that', 'she'): 1}
