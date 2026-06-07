# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tup):
    count = {}
    for word in tup:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

# words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
# print(count_words(words))

def average_prices(tup):
    total_price = {}
    count = {}
    for name, price in tup:
        if name in total_price:
            count[name] += 1
            total_price[name] += price
        else:
            count[name] = 1
            total_price[name] = price 
    average = {}
    for name in total_price:
        average[name] = total_price[name] / count[name]
    return average

# prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
# print(average_prices(prices))

def count_bigrams(tup):
    diction = {}
    for i in range(len(tup)-1):
        bigram = (tup[i], tup[i+1])
        if bigram in diction:
            diction[bigram] += 1
        else:
            diction[bigram] = 1
    return diction
        
# words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
# print(count_bigrams(words)) 


