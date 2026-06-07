def count_words(a:tuple):
    count={}
    for k in a:
        if k not in count:
            count[k] = 0
        count[k]+=1
    return count

#words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
#print(count_words(words))


def average_prices(a:tuple):
    average={}
    price={}
    number={}
    for k in a:
        if k[0] not in price:
            price[k[0]]=k[1]
            number[k[0]]=1
        else:
            price[k[0]]+=k[1]
            number[k[0]]+=1
        average[k[0]]=price[k[0]]/number[k[0]]
    return average

#prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
#print(average_prices(prices))

def count_bigrams(a:tuple):
    bigrams={}
    if len(a)<2:
        return {}
    for s in range(len(a)-1):
        if (a[s],a[s+1]) not in bigrams:
            bigrams[(a[s],a[s+1])]=1
        else:
            bigrams[a[s],a[s+1]]+=1
    return bigrams

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))