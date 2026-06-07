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

print(average_prices(prices))



