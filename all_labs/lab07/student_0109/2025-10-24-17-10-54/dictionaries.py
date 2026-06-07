#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def count_words(t):
    my_dict = {}
    for word in t:
        my_dict.update({word: 0})
    for word in t:
        if word in t:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
#print(count_words(words))

def average_prices(t):
    total_price = {}
    for item in t:
        total_price.update({item[0]: 0})
    for item in t:
        if item in t:
            total_price[item[0]] += item[1]

    total_number = {}
    for item in t:
        total_number.update({item[0]: 0})
    for item in t:
        if item in t:
            total_number[item[0]] += 1
    
    average = total_price.copy()
    for key in average:
        average[key] /= total_number[key]

    return average

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
#print(average_prices(prices))

def count_bigrams(t):
    my_dict = {}
    for i in range(0,len(t)-1):
        my_dict.update({(t[i],t[i+1]): 0})
    for i in range(0,len(t)-1):
        my_dict[(t[i],t[i+1])] += 1
    return my_dict

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
#print(count_bigrams(words))
