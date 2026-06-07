# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tuple):
    dict={}
    for word in tuple:
        if word not in dict:
            dict[word] = 1
        elif word in dict:
            dict[word]=int(dict[word]+1)
    return dict

def average_prices(tuple):
    dict={}
    counts = {}
    for pair in tuple:
        if pair[0] not in dict:
            dict[pair[0]]=pair[1]
            counts[pair[0]]=1
        elif pair[0] in dict:
            dict[pair[0]]=(pair[1]+dict[pair[0]])
            counts[pair[0]] += 1
    for key in dict:
        dict[key]=dict[key]/counts[key]
    return dict

def count_bigrams(tuple):
    dict={}
    for i in range(len(tuple) - 1):
        bigram = (tuple[i],tuple[i+1])
        if bigram not in dict:
            dict[bigram] = 1
        elif bigram in dict:
            dict[bigram]=int(dict[bigram]+1)
    return dict






