# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(words_tup):
    words_dict = {}
    
    for i in words_tup:
        if (i in words_dict):
            words_dict[i] += 1
        else:
            words_dict[i] = 1
    return words_dict

#words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
#print(count_words(words))

def average_prices(avg_p):
    total = {}
    count = {}
    averages = {}
    
    for item, price in avg_p:
        if (item in total):
            total[item] += price
            count[item] += 1
        else:
            total[item] = price
            count[item] = 1

    for item in total:
        averages[item] = total[item]/count[item]
    return averages

#prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
#print(average_prices(prices))

def count_bigrams(b_words):
    count = {}
    
    for i in range(len(b_words) - 1):
        bigram = (b_words[i], b_words[i + 1])
        if (bigram in count):
            count[bigram] += 1
        else:
            count[bigram] = 1
    return count

#words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
#print(count_bigrams(words))


