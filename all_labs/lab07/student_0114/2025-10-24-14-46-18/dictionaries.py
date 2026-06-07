# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(t):
    some_dict = {}
    for word in t:
        if not word in some_dict:
            some_dict[word] = 1
        else:
            some_dict[word] += 1
    return some_dict
        

#words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
#print(count_words(words))

def average_prices(lst):
    dict = {}
    occurences = {}
    for commodities in lst:
        if not commodities[0] in dict:
            dict[commodities[0]] = commodities[1]
            occurences[commodities[0]] = 1
        else:
            dict[commodities[0]] = (dict[commodities[0]] + commodities[1])
            occurences[commodities[0]] += 1
    for keys in dict:
        dict[keys] = dict[keys]/occurences[keys]
    return dict

#prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
#print(average_prices(prices))


def count_bigrams(many_words):
    dict = {}
    count = 0
    if len(many_words) > 2:
        while count < (len(many_words) - 1):
            key = (many_words[count], many_words[count+1])
            if key not in dict:
                dict[key] = 1
            else:
                dict[key] += 1
            count += 1
    return dict

#count_bigrams(())         # returns {}
#count_bigrams(('hello',)) # returns {} (note the trailing comma, which indicates
                          # this is a 1-element tuple instead of just a string)
#words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
#print(count_bigrams(words))