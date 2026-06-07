# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

#1
def count_words(words):
    some_dict = {}
    for word in words: 
       if word in some_dict:
            some_dict[word] += 1
       else:
            some_dict[word] = 1
    
    return some_dict

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

#2
# def average_prices(commodity_name, price):
#     total_price = {}
#     total_number_commodity_name = {}

#     for commodity_name, price in commodity_name, price: 
#        if commodity_name in total_price:
#             total_price[commodity_name] += price
#             total_number_commodity_name[commodity_name] += 1
#        else:
#             total_price[commodity_name] = price
#             total_number_commodity_name [commodity_name] = 1


#     average_prices_dict = {}
#     for commodity_name in total_price:
#         average_prices_dict[commodity_name]= total_price[commodity_name]/ total_number_commodity_name[commodity_name]
#         return average_prices_dict


def average_prices(input):
    total_number = {}
    commodity = {}

    for name,price in input:
        if name in commodity:
            commodity[name] += price
        else :
            commodity[name] = price

        if name in total_number:
            total_number[name] += 1
        else :
            total_number[name] = 1

    for name in commodity:
        commodity[name] = commodity[name] / float(total_number[name])

    return commodity

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))


#3.
def count_bigrams(words):
    bigram_count = {}
    
    if len(words)<2:
       return bigram_count
    
    for i in range(len(words)-1):
        bigram = (words[i],words[i+1])
        if bigram in bigram_count: 
            bigram_count[bigram]+= 1
        else:
             bigram_count[bigram]=1

    return bigram_count

print(count_bigrams(()))
print(count_bigrams(('hello',)))
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

