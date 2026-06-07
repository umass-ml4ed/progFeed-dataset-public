# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    D={}
    l=[]
    for i in words:
        if i not in l:
            l.append(i)
    for word in l:
        value=words.count(word)
        D[word]=value
    return D
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')

def average_prices(prices):
    d={}
    l=[]
    for x in prices:
        if x[0] not in l:
            l.append(x[0]) 
    for i in l:
        sum=0
        avg=0
        count=0
        for j in prices:
            if i==j[0]:
               sum+=j[1]
               count+=1
        avg=sum/count
        d[i[0]]=avg
    return d
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))


def count_bigrams(words):
    d={}
    l=[]
    for i in range(0,len(words)-1):
        tup=(words[i],words[i+1])
        if tup not in l:
            l.append(tup)
    for x in l:
        count=0
        for i in range(0,len(words)-1):
            new_tup=(words[i],words[i+1])
            if new_tup==x:
                count+=1
        d[x]=count
    return d
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))



