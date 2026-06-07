# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    dict={}
    for word in words:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    return dict

def average_prices(tup):
    tpd={} #total prices dictionary
    cpd={} #count dictionary(the p is for rhyming purposes) and it sounds like police departments 
    for item in tup:
        for i,j in item :
            if i in tpd:
                tpd[i]+=j
                cpd[i]+=1
            else:
                tpd[i]=j
                cpd[i]=1
    apd={} #average prices dictionary
    for i in tpd:
        apd[i]=tpd[i]/cpd[i]
    return apd

def count_bigrams(tup):
    bl=[] #bigram list
    for n in range(len(tup)-1):
        bl.append((tup[n],tup[n+1]))
    dic={}
    for i in bl:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return dic
