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
    totals = {}
    counts = {}
    for fruit, price in prices:
        totals[fruit] = totals.get(fruit, 0) + price
        counts[fruit] = counts.get(fruit, 0) + 1
    return {fruit: totals[fruit] / counts[fruit] for fruit in totals}

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
