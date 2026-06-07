# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(t):
    some_dict={}
    for w in t:
        if w not in some_dict:
            some_dict[w]=1
        else:
            some_dict[w]+=1
    return some_dict

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(t):
    total_price={}
    total_number={}
    for name, cost in t:
        if name in total_price:
            total_price[name]+=cost
            total_number[name]+=1
        else:
            total_price[name]=cost
            total_number[name]=1
    avg={}
    for name in total_price:
        avg[name]=total_price[name]/total_number[name] 
    return avg
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))


def count_bigrams(t):
    some_dict={}
    for index in range(len(t)-1):
        b=(t[index], t[index+1])
        if b not in some_dict:
            some_dict[b]=1
        else:
            some_dict[b]+=1
    return some_dict
print(count_bigrams(()))
print(count_bigrams(('hello',)))
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

        
        