# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    line = ""
    while n >= 1:
        ns = n
        for ns in range(n,0,-1):
            if ns == 1:
                line = line + str(ns) + "\n"
                break
            else: 
                line = line + str(ns) + " " 
                ns -= 1
        n -= 1
    return line

def merge_dicts(d1, d2):
    news = d1.copy()
    for key2 in d2:
        if key2 not in news:
            news[key2] = d2[key2]
        else:
            news[key2] = d2[key2] + d1[key2]
    return news     