# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(t):
    d = {}
    for i in t:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

def average_prices(t):
    d = {}
    for i in t:
        if i[0] in d:
            d[i[0]][1] += 1
            d[i[0]][0] += i[1]
        else:
            d[i[0]] = [i[1], 1]
    for i in d:
        d[i] = d[i][0] / d[i][1]
    return d

def count_bigrams(t):
    d = {}
    for i in range(len(t) - 1):
        if (t[i], t[i + 1]) in d:
            d[(t[i], t[i + 1])] += 1
        else:
            d[(t[i], t[i + 1])] = 1
    return d
