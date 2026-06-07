# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tup: tuple):
    result = {}
    for w in tup:
        if w not in result:
            result[w] = 1
        else:
            result[w] += 1
    return result

print(count_words(("word", "word", "word", "two", "two", "five", "one")))
print(count_words(('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')))

def average_prices(tup: tuple):
    count = {}
    total = {}
    for t in range(len(tup)):
        if tup[t][0] not in count:
            count[tup[t][0]] = 1
            total[tup[t][0]] = tup[t][1]
        else:
            count[tup[t][0]] += 1
            total[tup[t][0]] += tup[t][1]
    result = {}            
    for item in count:
        result[item] = total[item]/count[item]
    return result
    # return {result[item]: result[item]/count[item] for item in count}

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(tup: tuple):
    result = {}
    for s in range(len(tup)):
        if tup[s:s+2] not in result:
            result[tup[s:s+2]] = 1
        else:
            result[tup[s:s+2]] += 1
    return result
print(count_bigrams(('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')))