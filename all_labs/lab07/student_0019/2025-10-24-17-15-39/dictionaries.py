# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count 

def average_prices(total_price):
    total = {}
    for x, y in total_price:
        if x not in total:
            total[y] = [y, 1]
        else:
            total[x][0] += y
            total[x][1] += 1
            