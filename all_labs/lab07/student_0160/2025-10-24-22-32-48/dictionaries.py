# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tuple1:tuple):
    some_dict = {}
    for string in tuple1:
        if string in some_dict:
            some_dict[string]+=1
        else:
            some_dict[string]=1
    return some_dict

def average_prices(tuple2:tuple): 
    finalprices = {} 
    totalprice = {} 
    totalamount = {} 
    for item, price in tuple2:
        if item in totalprice:
            totalprice[item] += price
            totalamount[item] += 1
        else:
            totalprice[item] = price
            totalamount[item] = 1

    finalprices = {item: totalprice[item] / totalamount[item] for item in totalprice}
    return finalprices
