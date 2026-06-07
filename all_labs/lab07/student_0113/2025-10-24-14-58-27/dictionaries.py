#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def count_words(words):
    some_dict = {}
    for word in words:
        if word not in some_dict:
            some_dict[word] = 1
        else:
            some_dict[word] += 1 
    return some_dict


words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(items):
    values = {}
    total = {}
    for i in range(len(items)):
        if (items[i][0] not in values) and (items[i][0] not in total):
            values[items[i][0]] = items[i][1]
            total[items[i][0]] = 1 
        else:
            values[items[i][0]] += items[i][1]
            total[items[i][0]] += 1 
    for item, price in values.items():
        values[item] = price / total[item]

    return values

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(phrases):
    some_dict = {}
    for i in range((len(phrases)) -1):
        if len(phrases) > 2: 
            bigram = (phrases[i], phrases[i + 1])
        if bigram not in some_dict:
            some_dict[bigram] = 1
        else: 
            some_dict[bigram] += 1 
    return some_dict

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))
print(count_bigrams(()))         
print(count_bigrams(('hello',))) # returns {} (note the trailing comma, which indicates
                          