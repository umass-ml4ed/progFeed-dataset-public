# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(strings):
    words = {}
    for i in strings:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

#words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
#print(count_words(words))

def average_prices(names_and_prices):
    lists_of_prices = {}
    for name_and_price in names_and_prices:
        if name_and_price[0] not in lists_of_prices:
            lists_of_prices[name_and_price[0]] = [name_and_price[1]]
        else:
            lists_of_prices[name_and_price[0]].append(name_and_price[1])
    average_price_dict = {}
    for item in lists_of_prices:
        average_price_dict[item] = (sum(lists_of_prices[item]) / len(lists_of_prices[item]))
    return average_price_dict

#prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
#print(average_prices(prices))

def count_bigrams(words):
    bigrams = {}
    for index, word in enumerate(words):
        if index == (len(words) - 1):
            break
        firstnext = (word, words[index + 1])
        if firstnext not in bigrams:
            bigrams[firstnext] = 1
        else:
            bigrams[firstnext] += 1
    return bigrams

#words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
#print(count_bigrams(words))
