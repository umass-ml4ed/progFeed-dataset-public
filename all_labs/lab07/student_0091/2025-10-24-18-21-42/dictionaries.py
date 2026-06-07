# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED




words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
def count_words(words):
    some_dict= {}
    for word in words:
        if word in some_dict:
            some_dict[word] +=1
        elif word not in some_dict:
            some_dict[word]=1
    return some_dict

print(count_words(words))

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
def average_prices(prices)->dict:
    total_price={}
    total_item={}
    for item, price in prices:
        if item not in total_price:
            total_price[item]=price
            total_item[item]=1

        elif item in total_price:
            total_price[item]+=price
            total_item[item]+=1
    average={}

    for item in total_item:
        averagePrice=float(total_price[item])/float(total_item[item])
        average[item]=(averagePrice)

    return average
#Expected: {'a': 1.1, 'c': 4.2, 'b': 4.0, 'd': 10.4}
print(average_prices(prices))



words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
n=len(words)
def count_bigrams(words):
    bigram_list=[]
    word1_index=0
    word2_index=2
    i=0
    for word in words:
        bigram_list.append(words[word1_index:word2_index])
        word1_index+=1
        word2_index+=1
        i+=1
    #print(bigram_list)
    bigram_counter={}
    counter=0
    for bigram in bigram_list:
        if bigram not in bigram_counter:
            bigram_counter[bigram]=1
        elif bigram in bigram_counter:
            bigram_counter[bigram]+=1
    return bigram_counter


#Expected:{('she', 'knows'): 3, ('knows', 'and'): 1, ('and', 'she'): 1, ('knows', 'that'): 2, ('that', 'he'): 1, ('he', 'knows'): 1, ('that', 'she'): 1}
print(count_bigrams(words))


#Notes:
#print(words[0:2])
#print(words[1:3])


#this works like:
# start = 0
# stop = 2
# step = 1 (because not specified)




