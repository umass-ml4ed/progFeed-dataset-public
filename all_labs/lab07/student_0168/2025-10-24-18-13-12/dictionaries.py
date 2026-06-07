# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def count_words(tuple):
    some_dict={}
    for str in tuple:
        if str not in some_dict:
            some_dict[str]=1
        elif str in some_dict:
            some_dict[str]+=1
    return some_dict
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(price):
    avg_dict={}
    price_dict={}
    number_dict={}
    for value in price:
        key=value[0]
        cost=value[1]
        if key not in number_dict:
            number_dict[key]=1
            price_dict[key]=cost
        elif key in number_dict:
            number_dict[key]+=1
            price_dict[key]+=cost
    for key in price_dict:
        avg_dict[key]=price_dict[key]/number_dict[key]
    return avg_dict
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(words):
    some_dict={}
    count=0
    for wor in range(0, len(words)-1):
        word=words[count],words[count+1]
        if word in some_dict:
            some_dict[word]+=1
        elif word not in some_dict:
            some_dict[word]=1
        count+=1
    return some_dict
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))