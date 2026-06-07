# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(t):
    dict = {}
    for word in t:
        if (word not in dict):
            dict[word] = 1
        else:
            dict[word] += 1
    return dict

def average_prices(t):
    dictn = {}
    dictp = {}
    dict = {}
    index = 0
    while (index < len(t)):
        if (t[index][0] not in dict):
            dict[t[index][0]] = t[index][0]
            dictp[t[index][0]] = t[index][1]
            dictn[t[index][0]] = 1
        else:
            dictp[t[index][0]] += t[index][1]
            dictn[t[index][0]] += 1
        index += 1
    index = 0
    while(index < len(t)):
        dict[t[index][0]] = (dictp[t[index][0]] / dictn[t[index][0]])
        index += 1
    return dict

def count_bigrams(t):
    dict = {}
    index = 0
    if (len(t) > 1):
        while (index < len(t) - 1):
            if (t[index:(index + 2)] not in dict):
                dict[t[index:(index + 2)]] = 1
            else:
                dict[t[index:(index + 2)]] += 1
            index += 1
    else:
        return {}
    return dict


