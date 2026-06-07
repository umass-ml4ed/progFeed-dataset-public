# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tuple):
    d={}
    for word in tuple:
        if word not in d:
            d[word]=1
        else:
            d[word]+=1
    return d

def average_prices(comm):
    d={}
    for item in comm:
        if item[0] not in d:
            d[item[0]]=item[1]
        else:
            d[item[0]]=.5*(d[item[0]]+item[1])
    return d

def count_bigrams(tuple):
    d={}
    if len(tuple)>=2:
        for i in range(0,len(tuple)-1):
            if (tuple[i],tuple[i+1]) not in d:
                d[(tuple[i],tuple[i+1])]=1
            else:
                d[(tuple[i],tuple[i+1])]+=1
    return d

print(count_bigrams(()) )        # returns {}
print(count_bigrams(('hello',)))
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

