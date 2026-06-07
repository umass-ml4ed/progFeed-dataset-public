# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def count_words(lst):
    hash = {}
    for i in lst:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    return hash

def average_prices(t):
    cnt = {}
    hash = {}
    n=0
    for i in t:
        if i[0] in hash:
            cnt[i[0]]+=1
            hash[i[0]]+=i[1]
        else:
            cnt[i[0]]=1
            hash[i[0]]=i[1]
    for i,j in cnt.items():
        hash[i]/=j
    return hash


def count_bigrams(t):
    hash = {}
    for i in range(0,len(t)):
        if t[i:i+2] in hash:
            hash[t[i:i+2]]+=1
            print(t[i:i+2])
        else:
            hash[t[i:i+2]]=1
    return hash