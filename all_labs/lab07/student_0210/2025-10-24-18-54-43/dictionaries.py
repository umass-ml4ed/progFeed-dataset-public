# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
import math

def count_words(n):
    dictionary = {}
    for i in range(len(n)):
        word = n[i]
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


def average_prices(prices):
    total={}
    count={}
    for i in range(len(prices)):
        commodity = prices[i][1]
        price = prices[i][1]
        if commodity in total:
            total[commodity] += price
            count[commodity] += 1
        else:
            total[commodity] = price
            count[commodity] = 1

    averages = {}
    for commodity in total:
        averages[commodity] = round(total[commodity] / count[commodity],1)

    return averages

def count_bigrams(sentence):
    count = {}
    for i in range(len(sentence) - 1):
        bigram = (sentence[i], sentence[i+1])
        if bigram in count:
            count[bigram]+= 1
        else:
            count[bigram] = 1
    return count
