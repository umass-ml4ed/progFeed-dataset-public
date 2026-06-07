# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED


def count_words(words):
    
    word_counts = {}
    
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1 #adds it to the set with count 1
        
        else:
            word_counts[word] += 1 #if already in increases count
    
    return word_counts
    

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))



def average_prices(prices):
    
    total_prices = {}
    counts = {}
    
    for item, price in prices:
        if item not in total_prices:
            total_prices[item] = price
            counts[item] = 1
        else:
            total_prices[item] += price #adds total price of each item
            counts[item] += 1 #keeps track how many times item is in prices
            
    averages = {}
    for item in total_prices:
        averages[item] = total_prices[item] / counts[item]
        
    return averages
    
prices = (('a', 1.0),('c', 4.2),('b', 3.9),('a', 1.2),('d', 10.4),('b', 4.3),('b', 3.8))
print(average_prices(prices))


def count_bigrams(words):
    
    some_dict = {}
    
    for i in range(len(words)-1): #-1 because there must be following word
        
        bigram = (words[i], words[i + 1])
        
        if bigram not in some_dict:
            some_dict[bigram] = 1 
        else:
            some_dict[bigram] += 1
            
    return some_dict
    
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))