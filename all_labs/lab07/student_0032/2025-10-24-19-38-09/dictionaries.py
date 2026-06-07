# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def count_words(TUPLE: tuple): 
    someDict = {}
    for big_string in TUPLE:
        if big_string in someDict: 
            someDict[big_string] += 1
        else:
            someDict[big_string] = 1

    return someDict

#big_boss = ('fart', 'fart', 'shit', 'shit', 'hello', 'big')
#print(count_words(big_boss))

#words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
#print(count_words(words))


def average_prices(TUP: tuple):
    someDict = {}
    timesCalled = {}
    finalDict = {}

    for small_tuples in TUP: 

        item, price = small_tuples

        if item in someDict: 
            someDict[item] += float(price)
            timesCalled[item] += 1
        else: 
            someDict[item] = float(price)
            timesCalled[item] = 1
    
    for thingy in someDict:
        finalDict[thingy] = (someDict[thingy]) / (timesCalled[thingy])

    return finalDict

#new_words = (('gouda cheese 1 lbs', 3.49), ('organic oyster mushroom 1 lbs', 6.89), ('toilet paper 1 roll', 3.99), ('apple juice 1 gallon', 7.99), ('gouda cheese 1 lbs', 4.29), ('toilet paper 1 roll', 4.19), ('talenti gelato vanilla', 5.59))
#print(average_prices(new_words))
#prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
#print(average_prices(prices))


def count_bigrams(TUP: tuple): 
    stupid_list = []
    someDict = {}
    
    for n in range(len(TUP)-1):
        stupid_list.append((TUP[n], TUP[n+1]))
    #for string in TUP:
    #   if string[0] 

    for duo in stupid_list: 
        if duo in someDict:
            someDict[duo] += 1
        else: 
            someDict[duo] = 1

    return someDict

newest_words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows', 'arvid')
print(count_bigrams(newest_words))