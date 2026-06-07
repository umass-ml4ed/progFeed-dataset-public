# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(x):
    d={}
    for a in x:
        if a not in d:
            d[a]=1
        else:
            d[a]+=1
    return(d)
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))


#def average_prices():
#def count_bigrams():