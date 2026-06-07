# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words (words): 
    somed = {}
    for i in words: 
        if i in somed: 
            somed[i] = somed[i] + 1
        else: 
            somed[i] = 1 
    return somed

def average_prices(things):
    price = {}
    number = {}
    for i, p in things: 
        if i in number:
          number[i] = number[i] + 1
        else: 
            number[i] = 1
        
        if i in price: 
            price[i] = price[i] + p
        else: 
            price[i] = p
    
    avg = {i: price[i]/number[i] for i in price}
    return avg

def count_bigrams(words): 
    dic = {}
    for i in range(len(words)-1): 
        bi = (words[i], words[i+1])
        if bi in dic: 
            dic[bi] = dic[bi]+1
        else:
            dic[bi] = 1 
        
    return dic

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))





