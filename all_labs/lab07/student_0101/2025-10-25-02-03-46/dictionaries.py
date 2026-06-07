# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    some_dict={}
    print(words)
    for i in words:
        if i in some_dict:
            some_dict[i]+=1
        else:
            some_dict[i] = 1
    return some_dict
def average_prices(groceries):
    price={}
    count={}
    average={}
    for i, p in groceries:
        if i in price:
            price[i]+= p
            count[i]+=1
        else:
            price[i]= p
            count[i]= 1
    for item in price:
        average[item]=price[item]/count[item]
    return average