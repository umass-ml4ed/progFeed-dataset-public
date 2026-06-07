# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(my_tuple):
    my_dict = {}
    for i in my_tuple:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    return my_dict
    
my_tuple = ("he", "saw", "a", "saw", "a")
print(count_words(my_tuple))

def average_prices(prices):
    t = {}
    c = {}
    for i, j in prices:
        if i not in t:
            t[i] = j
            c[i] = 1
        else:
            t[i] += j
            c[i] += 1
    average = {}
    for i in t:
        average[i] = t[i] / c[i]

    return average

prices = (('a', 1.0), 
        ('c', 4.2), 
        ('b', 3.9), 
        ('a', 1.2), 
        ('d', 10.4), 
        ('b', 4.3), 
        ('b', 3.8))

print(average_prices(prices))

def count_bigrams(words):
    bigrams = {}
    for i in range(0, len(words) - 1):
        new = (words[i], words[i +1])
        if new in bigrams:
            bigrams[new] +=1
        else:
            bigrams[new] = 1
    return bigrams
