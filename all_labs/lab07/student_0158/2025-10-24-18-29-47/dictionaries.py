# Authors   : REDACTED
# Emails    : REDACTED
# Spire ID REDACTED

def count_words(t):
    d={}
    for i in t:
        if i not in d:
            d.update({i:1})
        else:
            d.update({i:d[i]+1})
    return d

words = ('we', 'i', 'blaaa', 'i', 'we', 'booeo', 'blaaa')
print(count_words(words))
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(t):
    dt={}
    list=[]
    for i in t:
        if i[0] in dt:
            dt[i[0]]+=i[1]
        else:
            dt[i[0]]=i[1]
    dn={}
    for i in t:
        if i[0] in dn:
            dn[i[0]]+=1
        else:
            dn[i[0]]=1
    da={}
    for i in dt:
        da.update({i:dt[i]/dn[i]})
    return da

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))
print(average_prices((('gouda cheese 1 lbs', 3.49), ('organic oyster mushroom 1 lbs', 6.89), ('toilet paper 1 roll', 3.99), ('apple juice 1 gallon', 7.99), ('gouda cheese 1 lbs', 4.29), ('toilet paper 1 roll', 4.19), ('talenti gelato vanilla', 5.59))))

def count_bigrams(t):
    d={}
    for i in range(1, len(t)):
        if (t[i-1], t[i]) not in d:
            d.update({(t[i-1], t[i]):1})
        else:
            d.update({(t[i-1], t[i]):d[(t[i-1], t[i])]+1})
    return d
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))
print(count_bigrams(()))  
print(count_bigrams('h', ))
print(count_bigrams(('what', 'is', 'your', 'problem', 'because', 'your', 'problem', 'is', 'my', 'problem')))