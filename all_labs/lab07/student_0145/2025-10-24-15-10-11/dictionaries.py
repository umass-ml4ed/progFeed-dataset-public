# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

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

def average_prices(prices):
   
 some_dict = {}

 for name, price in prices:

    if name in some_dict:
       
       some_dict[name].append(price)
    
    else: 
       
       some_dict[name] = [price]
                          
    averages = {}

    for name in some_dict:
       
       avg_price = sum(some_dict[name]) / len(some_dict[name])

       averages[name] = avg_price 

    return averages
 
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(words):
   
    some_dict = {}

    if ln(words) < 2:
       
       return some_dict
    
    for i in range(len(words)- 1):
       
       bigram = (words[i], words[i +1])

       if bigram in some_dict:
          
          some_dict [bigram] += 1

       else: 
          
          some_dict[bigram] += 1

    return some_dict 
