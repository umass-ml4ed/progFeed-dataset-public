# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def count_words(a : tuple):
    result = {}
    for words in a:
        if (words in result):
            result[words] += 1
        else :
            result[words] = 1
    return result


# words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
# print(count_words(words))
        

def average_prices(a):
    d1 = {}
    d2 = {}
    l1 = len(a)
    for item in a:
        if (item[0] in d1):
            d1[item[0]] += item[1]
            d2[item[0]] += 1
        else :
            d1[item[0]] = item[1]
            d2[item[0]] = 1

    for b in d1:
        d1[b] = d1[b]/(d2[b])

    return d1


# prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
# print(average_prices(prices))


def count_bigrams(a):
    result = {}
    l1 = len(a) 
    for words in range (0,(l1-1)):
        w1 = a[words]
        w2 = a[words+1]

        tupletoadd = (w1,w2)
        if tupletoadd in result:
            result[tupletoadd] += 1
        else :
            result[tupletoadd] = 1
    
    return result


words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))