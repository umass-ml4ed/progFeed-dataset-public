# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(tup): 
    some_dict = {}
    for word in tup: 
        if word not in some_dict: 
            some_dict[word] = 1
        else: 
            some_dict[word] += 1
    return some_dict 

def average_prices(big_tup): 
    some_dict = {}
    for small_tup in big_tup: 
        if small_tup[0] in some_dict: 
            some_dict[small_tup[0]].append(small_tup[1])
        else: 
            some_dict[small_tup[0]] = [small_tup[1]]
    return {key: sum(some_dict[key])/len(some_dict[key]) for key in some_dict}

def count_bigrams(tup): 
    some_dict = {}
    for i in range (len(tup)-1): 
        bigram = (tup[i], tup[i+1]) 
        if bigram not in some_dict:
            some_dict[bigram] = 1
        else: 
            some_dict[bigram] += 1
    return some_dict 

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))


        