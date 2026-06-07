# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(tuple_of_strings):
    some_dict = {}
    for string in tuple_of_strings:
        if string not in some_dict:
            some_dict[string] = 1
        else:
            some_dict[string] += 1
    return some_dict

def average_prices(tuple_of_commodities_prices):
    total_price = {}
    total_number = {}
    for item in tuple_of_commodities_prices:
        food = item[0]
        price = item[1]
        if food in total_price:
                total_price[food] += price
                total_number[food] += 1
        else:
                total_price[food] = price
                total_number[food] = 1
    for element in total_price:
        total_price[element] = total_price[element] / total_number[element]
    
    return total_price

def count_bigrams(tuple_of_words):
    some_dict = {}
    for element in range(len(tuple_of_words) -1):
        words = tuple_of_words[element], tuple_of_words[element + 1] 
        if words not in some_dict:
            some_dict = 1
    return count_bigrams

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

         


        
  
