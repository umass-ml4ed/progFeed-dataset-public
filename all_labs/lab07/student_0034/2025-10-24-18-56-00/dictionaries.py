# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(t):
    word_dict = {}
    for word in t:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

#words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
#print(count_words(words))

def average_prices(coms):
    dict_p = {}
    dict_n = {}
    for tup in coms:
        if tup[0] not in dict_p:
            dict_p[tup[0]] = tup[1]
            dict_n[tup[0]] = 1
        else:
           dict_p[tup[0]] += tup[1]
           dict_n[tup[0]] += 1
    for key in dict_n:
        dict_p[key] = dict_p[key] / dict_n[key]
    return dict_p

#prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
#print(average_prices(prices))

def count_bigrams(t):
    bi_dict = {}
    it = 0
    for word in range(0,len(t)-1):
        if (t[it],t[it+1]) not in bi_dict:
            bi_dict[(t[it],t[it+1])] = 1
            it += 1
        else:
            bi_dict[(t[it],t[it+1])] += 1
            it += 1
    return bi_dict


#words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
#print(count_bigrams(words))