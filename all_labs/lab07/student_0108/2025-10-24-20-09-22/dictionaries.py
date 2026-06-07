# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(word_tup):
    i=0
    some_dict={}
    for word in word_tup:
        if(word not in some_dict):
            some_dict[word]=1
        else:
            some_dict[word]+=1
        
    return some_dict

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
#print(count_words(words))

def average_prices(comm_tup):
    price_dict={}
    for tup in comm_tup:
        commodity=tup[0]
        price=tup[1]

        if(commodity not in price_dict):
            price_dict[commodity]=[price]
        else:
            price_dict[commodity].append(price)

    avg_price={}
    for comm in price_dict:
        avg_price[comm]=sum(price_dict[comm])/len(price_dict[comm])

    return avg_price
    """"
    new_dict={}
    price_dict={}
    numb_tup={}

    for tup in comm_tup:    
    
    for tup in comm_tup:
        if(tup[0] not in new_dict):
            new_dict[tup[0]]=[tup[1]]
        else:
            new_dict[tup[0]].append(tup[1])

            price_lst.append(tup[1])
            avg=sum(price_lst)/len(price_lst)
            new_dict[tup[1]]=avg
    return new_dict"""
    
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(word_tup):
    some_dict={}
    bigram_tup=()
    if(len(word_tup)<2):
        return some_dict
    else:
        for i in range(len(word_tup)-1):
            bigram_tup=(word_tup[i],word_tup[i+1])
            if(bigram_tup not in some_dict):
                some_dict[bigram_tup]=1
            else:
                some_dict[bigram_tup]+=1

        return some_dict
        
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
#print(count_bigrams(words))