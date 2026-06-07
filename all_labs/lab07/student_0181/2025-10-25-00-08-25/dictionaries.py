# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(a):
    some_dict = {}
    for i in a : 
        if i not in some_dict:
            some_dict[i] = 1
        else: 
            some_dict[i] += 1 
    return some_dict

def average_prices(a):
    count = {}
    totals = {}
    for i in range(len(a)):
        name = a[i][0]
        price = a[i][1]

        if name in totals:
            totals[name] = totals[name]+ price
            count[name]= count[name]+1
        else:
            totals[name] = price
            totals[name]=1
    
        avrages = {}
        for name in totals:
            avrages[name] = round(totals[name]/counr[name],1)
    return avrages

def count_bigrams(words):
    count = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in count:
            count[bigram] += 1
        else:
            count[bigram] = 1
    return count
 

