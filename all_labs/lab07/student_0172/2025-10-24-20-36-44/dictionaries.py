# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    amount = {}
    for word in words:
        if word in amount:
            amount[word] += 1
        else:
            amount[word] = 1
    return amount

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))