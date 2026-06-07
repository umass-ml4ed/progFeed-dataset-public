# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def most_frequent_element(list):
    d={}
    for item in list:
        if item in d:
            d[item]+=1
        else:
            d[item]=1

    max_k=None
    max_v=0

    for k,v in d.items():
        if v>max_v:
            max_v=v
            max_k=k
    
    return max_k
