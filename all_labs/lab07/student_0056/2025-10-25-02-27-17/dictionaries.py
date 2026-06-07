# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')


def count_words(tupple):
    some_dict={}
    for i in tupple:
        some_dict[i] = 0
    for i in tupple:
        if i in tupple:
            some_dict[i] += 1
    return some_dict
    
print(count_words(words))


prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))


def average_prices(l):
    avrg_pric = {}
    for i in l:
        avrg_pric[i[0]] = []
    for i in l:
        if i[0] in avrg_pric:
            avrg_pric[i[0]].append(i[1])
    for i in avrg_pric:
        avrg_pric[i] = sum(avrg_pric[i])/len(avrg_pric[i])
    return avrg_pric
   


print(average_prices(prices))

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')

def count_bigrams(t):
    diction = {}
    for i in range(len(t)-1):
        diction[(t[i], t[i+1])] = 0
    for i in range (len(t)-1):
        if (t[i], t[i+1]) in diction:
            diction[(t[i], t[i+1])] += 1
    return diction

print(count_bigrams(words))
 
