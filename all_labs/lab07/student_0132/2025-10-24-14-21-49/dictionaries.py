# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(a):
    new = {}
    for value in a:
        if value in new:
            new[value] += 1
        else:
            new[value] = 1
    return new

def average_prices(col):
    totprice = {}
    totnumber = {}
    for name, price in col:
        if name in totprice:
            totprice[name] = totprice.get(name) + price
        else:
            totprice[name] = price
        if name in totnumber:
            totnumber[name] = totnumber.get(name) + 1
        else:
            totnumber[name] = 1
    avg = {}
    for name in totprice:
        avg[name] = totprice[name]/totnumber[name]
    return avg

def count_bigrams(lst):
    bigrams = {}
    for i, e in enumerate(lst):
        if i != len(lst) - 1:
            if ((e,lst[i+1])) not in bigrams:
                bigrams[(e,lst[i+1])] = 1
            else:
                bigrams[(e,lst[i+1])] += 1
        else:
            break
    return bigrams
