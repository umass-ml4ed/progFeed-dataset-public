#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def count_words(tuple_of_strings):
    some_dict={}
    for word in tuple_of_strings:
        if word not in some_dict:
            some_dict[word]=1 
        else:
            some_dict[word]+=1
    return some_dict 

def average_prices(commodity):
    total_price= {}
    total_number={}
    for item, price in commodity: 
        if item not in total_price:
            total_price[item]= price 
            total_number[item]= 1 
        else:
            total_price[item]+= price
            total_number[item]+= 1
    average= {}
    for item in total_price:
        average[item]= total_price[item]/ total_number[item]
    return average 

def count_bigrams(tuple_of_words):
    some_dict={}
    for word in range(len(tuple_of_words)-1):
        bigram={tuple_of_words[word], tuple_of_words[word +1]}
        if bigram not in some_dict:
            some_dict[bigram]= 1
        else:
            some_dict[bigram]+= 1
    return some_dict