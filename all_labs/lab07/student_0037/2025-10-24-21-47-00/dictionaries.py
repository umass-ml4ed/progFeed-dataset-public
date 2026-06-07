# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(mytuple):
    some_dict = {}
    for word in mytuple:
        if word not in some_dict:
            some_dict[word] = 1 
        else:
            some_dict[word] += 1 
    return some_dict

def average_prices(commodity_list):
    totalPrice = {}
    totalNumber = {}
    averagePrice = {}
    #loop over commodity list, find key, count total number
    for item in commodity_list:
        if item [0] not in commodity_list:
            totalNumber[item[0]] = 1 
        else: 
            totalNumber[item[0]]+= 1 
    #loop over commodity list, find key, add total value
    for item in commodity_list:
        if item[0] not in totalPrice:
            totalPrice[item[0]] = item[1]
        else:
            totalPrice[item[0]] += item[1]
    #loop over total price and total number, divide price by number
    for item in commodity_list:
        if item[0] not in averagePrice:
            averagePrice[item[0]] = totalPrice[item[0]] / totalNumber[item[0]]
    return averagePrice

def count_bigrams(myTuple):
    someDict = {}
    for i in range(0, len(myTuple)-1):
        first = myTuple[i]
        next = myTuple[i+1]
        bigram = (first, next)
        if bigram not in someDict:
            someDict[bigram] = 1
        else:
            someDict[bigram] += 1 
    return someDict

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))






            


