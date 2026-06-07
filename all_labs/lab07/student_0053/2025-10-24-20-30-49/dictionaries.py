# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words: tuple) -> dict:
    dic = {}
    for i in words:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic


def average_prices(commondity):
    dic_commondity = {}
    for i in commondity:
        if i[0] in dic_commondity:
            dic_commondity[i[0]].append(i[1])
        else:
            dic_commondity[i[0]] = []
            dic_commondity[i[0]].append(i[1])
    dic_average = {}
    for i in dic_commondity:
        dic_average[i] = sum(dic_commondity[i])/len(dic_commondity[i])
    return dic_average


def count_bigrams(words):
    dic_bigram = {}
    for i in range(0, len(words) - 1):
        bigram = (words[i], words[i+1])
        if bigram in dic_bigram:
            dic_bigram[bigram] += 1
        else:
            dic_bigram[bigram] = 1
    return dic_bigram

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))



